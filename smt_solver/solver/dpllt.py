
from solver.theory import SAT, QF_LRA #, QF_LIA
from solver.common import types
from solver.formula import cnf_manager

import time

class dpllt_solver_s(object):
    def __init__(self):
        # state: -1, unknown; 0, false; 1, true
        self.state = -1

        # assertion stack
        self.assertions_stack = None
        self.reset_assertions()

        # Maps Symbol to inside variable (represented as index)
        self.symbol_to_decl = {}
        # variables dictionary: (idx, var)
        self.var_table = {}

        # sort stack: record old or new type
        self.sorts = set()
        # internal sort
        self.sorts.add(types.BOOL)
        self.sorts.add(types.REAL)
        self.sorts.add(types.INT)
        self.sorts.add(types.STRING)

        # record the theory formula, maps constraint to index
        self.skeletonStack = [None]
        # maps literal to formula stack index
        self.skeletonMaps = {}
        # maps constraints to literal
        self.literalMaps = {}
        # literal manager
        self.cnf_mgr = cnf_manager(self)

        # core theory solver setting
        # if init here, must consider when pop -> reset (semi-incremental)
        self.sat_solver = SAT.solver()
        # maps Bool variable(string) to literal
        self.sat_variable = {}
        # theory solver: sovler-solve problem;
        self.theory_solver = None
        # record +/- constraint appended to theory_solver
        self.theory_history = []

        # record solving time
        self.time = 0

    # 复位dpllt求解器
    def reset_dpllt(self):
        self.state = -1

        # assertion stack
        self.assertions_stack = None
        self.current_assertions_level = 0
        self.reset_assertions()

        # self.backtrack = []
        # self.latest_model = None

        # Maps Symbol to inside variable (represented as index)
        self.symbol_to_decl = {}
        # variables dictionary: (idx, var)
        self.var_table = {}
        # let area, map let var to its litrals(single)
        self.var_bings = {}
        # let x (..), the x must used, or an error may be happen

        # sort stack: record old or new type
        self.sorts = set()
        # internal sort
        self.sorts.add(types.BOOL)
        self.sorts.add(types.REAL)
        self.sorts.add(types.INT)
        self.sorts.add(types.STRING)

        # record the theory formula, maps constraint to index
        self.skeletonStack = [None]
        # maps literal to formula stack index
        self.skeletonMaps = {}
        # maps constraints to literal
        self.literalMaps = {}
        # literal manager
        self.cnf_mgr = cnf_manager(self)

        # core theory solver setting
        # if init here, must consider when pop -> reset (semi-incremental)
        self.sat_solver = SAT.solver()
        # maps Bool variable(string) to literal
        self.sat_variable = {}
        # theory solver: sovler-solve problem;
        self.theory_solver = None
        # record +/- constraint appended to theory_solver
        self.theory_history = []

    # 复位断言
    def reset_assertions(self):
        self.assertions_stack = []
        self.current_assertions_level = 0

    # 声明变量 
    def declare_variable(self, var):
        if not var.is_symbol():
            print("Trying to declare as a variable something "+"that is not a symbol: %s" % var)
        # 如果未声明过
        if var not in self.symbol_to_decl:
            # 添加变量
            self.add_variable(var.symbol_name(), var.get_type())
    
    # 添加断言
    def add_assertion(self, clause, named=None):
        # 添加约束
        self.assertions_stack.append(clause)
        self.state = -1

    # 求解
    def solve(self, assumptions=None):
        self.time = time.clock()
        if(self.state==0): return False
        
        if(assumptions is not None):
            print("not support!")

        # error
        if(self.check_assertions()):
            self.sat_solver = SAT.solver(Clauses = self.all_cnf(), nVars = self.cnf_mgr.get_max())
        else:
            self.state = 0
            return False

        # DPLL(T) structure
        while(True):
            if(not self._check_units()): 
                self.time = time.clock()-self.time
                return False # cannot propagate, conflicts in clauses
            if(self._check_assignment()): 
                self.time = time.clock()-self.time
                return True # if full assignment => True
            
    # 判断赋值是否可满足
    def _check_assignment(self):
        # check whether the assignment is sat under theory solver
        # from self._check_units -> self._check_assignment => self.theory_solver must have returned True
        if(self.sat_solver.satisfied()):
            self.state = 1
            return True # sat under theory + full assignment -> return true
        else:
            # sat under theory + not full assignment -> return False, go on finding(decide)
            self.sat_solver.decide()
            return False

    # 赋值
    def _check_units(self):
        # check an SMT assignment is true or false, which deduced by sat solver
        units = []
        while(True):
            # find unit clauses(assignment) for theory solver
            while(True):
                units = self.sat_solver.propagate()
                if(units is None): 
                    # cannot find a partial assignment, conflicts in clauses
                    self.state = 0
                    return False
                elif(len(units)==0): continue # sat solver restart for a new propagate answer
                else: break # sat solver find a new solution
            # test the partial assignment in theory solver
            # if this partial assignment is wrong currently
            conflicts, add_success = self.setTheoryConstraints(units)
            # add constraint errors
            solve_success = False
            if(add_success):
                conflicts, solve_success = self.theory_solver.solve()
            if(solve_success):
                # the partial assignment is sat
                # add implication to sat sovler for exploring
                # now not append for it is not tautology
                # if you want to append this, must implement delete clause in SAT solver
                # self.sat_solver.add_clause(conflicts) 
                return True
            # the partial assignment conflicts under theory solver
            # add theory conflicts to sat solver
            self.sat_solver.add_clause([-i for i in conflicts])
            # theory history must clear, for constraints may be different
            self.theory_history = []
            # theory solver must reset, for constraint may be different
            self.theory_solver.reset()
            # sat solver must restart, for a new clause is appended
            self.sat_solver.restart()
    
    # 检查断言
    def check_assertions(self):
        for i in self.assertions_stack:
            for j in i:
                if(self.cnf_mgr.is_false(j)):
                    return False
        return True
    
    # 
    def setTheoryConstraints(self, model):
        # record appending history, only theory literals but not auxiliary variable
        for i in model:
            if(abs(i) in self.skeletonMaps):
                if(i not in self.theory_history):
                    # current result of check-sat is still True, go on
                    self.theory_history.append(i)
                    lits, ans = self.theory_solver.add_constraint(self.skeletonStack[self.skeletonMaps[abs(i)]], i)
                    # add constriants errors
                    if(not ans):
                        return lits, ans
        return None, True
                
    # this method is called by SAT solver to check a partial assignment for T-consistentcy
    def deduce(self):
        pass

    def get_value(self, item):
        pass
    
    # 输出变量赋值
    def get_answer(self):
        if(self.state==1):
            base_model = self.theory_solver.get_model()
            ans = ""
            for i in self.symbol_to_decl:
                if(i in self.sat_variable):
                    # it is a sat variable
                    var = self.sat_variable[i]
                    ans += ("(declare-const %s %s %s)"%(i, str(self.symbol_to_decl[i]["sort"]), str(self.sat_solver.literals[var].is_true())))
                    ans += "\n"
                else:
                    # it is a theory variable
                    ans += ("(declare-fun %s %s %s)"%(i, str(self.symbol_to_decl[i]["sort"]), str(base_model[i])))
                    ans += "\n"
            return ans[:-1]
        return ""

    # 
    def push(self, levels=1):
        for _ in range(levels):
            self.backtrack.append(len(self.assertions_stack))

    # 
    def pop(self, levels=1):
        self.state = -1
        for _ in range(levels):
            l = self.backtrack.pop()
            self.assertions_stack = self.assertions_stack[:l]

    # 获取断言栈的长度
    def get_asserts_length(self):
        return len(self.assertions_stack)

    def _exit(self):
        print("exit")

    # 选择合适的求解器
    def setLogic(self, symbol):
        # if(symbol == "QF_LIA"):
        #     print("Not support!")
        #     # self.theory_solver = QF_LIA.solver()
        #     # self.theory_calculation = QF_LIA.calculation
        #     # self.theory_constraint = QF_LIA.constraint
        if(symbol == "QF_LRA"):
            self.theory_solver = QF_LRA.solver()
        else:
            print("when set-logic %s, errors happend"%symbol)

        # update formula stack in converter.convert -> maps formula to literal index
        # self.theory_converter.setFormulas(self.formulaStack)

    # 添加约束
    # called by deduce() to add a clause as a consequence of assignment
    def add_clause(self, clause):
        # only append a single clause
        self.sat_solver.add_clause(clause)

    # called to communicate a T-implication to the SAT solver
    def theory_implication(self, constraints):
        # convert constraints to literals
        pass

    # 添加变量，sym:符号名字; sar:符号类型
    # from now on, auxiliary functions
    def add_variable(self, sym, sor):
        try:
            # 若sor属于支持的类型
            if(sor in self.sorts):
                # must a declared type
                if(sym in self.symbol_to_decl):
                    # already declared -> error
                    raise DuplicateDefinition()
                elif(sor != "Bool"):
                    self.theory_solver.add_variable(sym)
                else:
                    # type bool
                    var = self.cnf_mgr.make_literal()
                    self.sat_variable[sym] = var
                index = len(self.var_table)
                self.var_table[index] = sym
                self.symbol_to_decl[sym] = {
                    "index": index,
                    "sort": sor
                }
                return sym
            else:
                print("Type %s not defined." % sor)
                raise SyntaxError()
        except DuplicateDefinition:
            print("Duplicate Definition about variable %s" % sym)

    # 
    def all_cnf(self, level=0):
        ans = []
        for idx in range(level, len(self.assertions_stack)):
            ans.append(self.assertions_stack[idx])
        self.current_assertions_level = len(self.assertions_stack)
        return ans


class DuplicateDefinition(Exception):
    pass


if(__name__ == "__main__"):
    # 3. function propagate in SAT.solver
    # 4. function deduce, theory_implication in QF_LRA.solver
    # run in this main, and next to smt_solver.py -> success
    s=dpllt_solver_s()
    print(s)