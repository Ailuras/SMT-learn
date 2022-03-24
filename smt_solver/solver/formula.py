from decimal import Decimal
from solver.theory import SAT # , QF_LIA
from solver.theory.QF_LRA import calculation as LA_calculation
from solver.theory.QF_LRA import constraint as LA_constraint
from solver.theory.QF_LRA import to_calculation as to_LA_calculation

class operator(object):
    def __init__(self, solver = None):
        self.smt_solver = solver

        # auxiliary structure
        self.sat_solver = self.smt_solver.sat_solver
        self.skeleton_stack = self.smt_solver.skeletonStack
        self.skeleton_map = self.smt_solver.skeletonMaps
        self.literal_map = self.smt_solver.literalMaps

        # literal manager
        self.cnf_mgr = self.smt_solver.cnf_mgr

    
    def ADD(self,formula):
        # A single unit clause happens when it is a single theory formula or single and, or, not
        self.smt_solver.add_assertion([formula])

    def AND(self, *params):
        return self.cnf_mgr.land_list(params)

    def OR(self, *params):
        return self.cnf_mgr.lor_list(params)

    def NOT(self, var):
        return self.cnf_mgr.lnot(var)

    def XOR(self, *params):
        return self.cnf_mgr.lxor_list(params)

    def IMPLY(self, *params):
        assert(len(params)>=2)
        return self.cnf_mgr.limplies(params[0], params[1])

    def ITE(self, *params):
        assert(len(params)>=3)
        return self.cnf_mgr.lselect(params[0], params[1], params[2])

    def IFF(self, *params):
        assert(len(params)>=2)
        return self.cnf_mgr.lequal(params[0], params[1])
    
    # LA arithmetic operator
    def check_op(self, cons):
        if(cons in self.literal_map):
            return self.literal_map[cons]
        else:
            lit = self.cnf_mgr.make_literal()
            idx = len(self.skeleton_stack)
            self.skeleton_stack.append(cons)
            self.skeleton_map[lit] = idx
            self.literal_map[cons] = lit
            return lit

    def LT(self, a, b):
        tcons = LA_constraint(l=a,r=b,opr="<")
        return self.check_op(tcons)

    def LE(self, a, b):
        tcons = LA_constraint(l=a,r=b,opr="<=")
        return self.check_op(tcons)

    def GT(self, a, b):
        tcons = LA_constraint(l=a,r=b,opr=">")
        return self.check_op(tcons)

    def GE(self, a, b):
        tcons = LA_constraint(l=a,r=b,opr=">=")
        return self.check_op(tcons)

    def EQ(self, a, b):
        tcons1 = LA_constraint(l=a,r=b,opr=">=")
        tcons2 = LA_constraint(l=a,r=b,opr="<=")
        l1 = self.check_op(tcons1)
        l2 = self.check_op(tcons2)
        return self.AND(l1, l2)
        # tcons = LA_constraint(l=a, r=b, opr="=")
        # return self.check_op(tcons)

    def plus(self, *params):
        assert(len(params)>0)
        answer = LA_calculation()
        for i in params:
            answer = answer + i
        return answer

    def minus(self, *params):
        if(len(params)==1):
            # -a
            a = to_LA_calculation(params[0])
            return -a
        else:
            # a-b
            a = to_LA_calculation(params[0])
            b = to_LA_calculation(params[1])
            return a-b

    def times(self, a, b):
        a = to_LA_calculation(a)
        b = to_LA_calculation(b)
        return a*b

    def divide(self, a, b):
        a = to_LA_calculation(a)
        b = to_LA_calculation(b)
        return a/b



class literal(int):
    def __init__(self, val=0):
        super(literal, self).__init__()
        self.val = val

class cnf_manager(object):
    # for literal is judge by -1 or 0 or 1
    # so index starts from 2
    def __init__(self, solver=None, index = 2):
        self.__index = index
        self.solver = solver

    def get_max(self):
        return self.__index

    def make_literal(self):
        var = literal(int(self.__index))
        self.__index += 1
        return var

    def pos(self, lit):
        return literal(lit)
    
    def neg(self, lit):
        return literal(-lit)

    def lcnf(self, lits):
        stat, clause = self.process_clause(lits)
        lent = len(clause)
        if(lent==0):
            if(stat): return # True, [] -> clause = True 
            else: print("error in add_assertion")
        elif(lent==1):
            if(stat): print("error in add_assertion")
            else: self.solver.add_assertion(clause)
        else: self.solver.add_assertion(clause)

    def process_clause(self, clause):
        if(type(clause) != list):
            if(self.is_true(clause)): return True, []
            if(self.is_false(clause)): return False, [self.const_literal(False)]
            return False, [clause]
        ans = []    
        for i in clause:
            if(self.is_true(i)): return True, []
            if(self.is_false(i)): continue
            if(i not in ans): ans.append(i)
            if(-i in ans): return True, []
        
        return False, ans

    def land(self, a, b):
        if(self.is_true(a)): return b
        if(self.is_true(b)): return a
        if(self.is_false(a)): return self.const_literal(False)
        if(self.is_false(b)): return self.const_literal(False)

        lit = self.make_literal()
        self._internal_land(a, b, lit)
        return lit

    def lor(self, a, b):
        if(self.is_false(a)): return b
        if(self.is_false(b)): return a
        if(self.is_true(a)): return self.const_literal(True)
        if(self.is_true(b)): return self.const_literal(True)

        lit = self.make_literal()
        self._internal_lor(a, b, lit)
        return lit

    def lnot(self, a):
        return self.neg(a)

    def lxor(self, a, b):
        if(self.is_false(a)): return b
        if(self.is_false(b)): return a
        if(self.is_true(a)): return self.lnot(b)
        if(self.is_true(b)): return self.lnot(a)

        lit = self.make_literal()
        self._internal_lxor(a, b, lit)
        return lit

    def lnand(self, a, b):
        return self.lnot(self.land(a, b))

    def lnor(self, a, b):
        return self.lnot(self.lor(a, b))

    def lequal(self, a, b):
        return self.lnot(self.lxor(a, b))

    def limplies(self, a, b):
        return self.lor(self.lnot(a), b)

    def lselect(self, a, b, c):
        if(self.is_true(a)): return b
        if(self.is_false(a)): return c
        if(b==c): return b

        f = self.land(a, b)
        s = self.land(self.lnot(a), c)
        return self.lor(f, s)

    def land_list(self, params):
        # degenerate when size = 0, 1, 2
        if(len(params)==0): return self.const_literal(True)
        if(len(params)==1): return params[0]
        if(len(params)==2): return self.land(params[0], params[1])

        for i in params:
            if(self.is_false(i)): return self.const_literal(False)
        
        ans = self.eliminate_duplicates(params)
        lit = self.make_literal()

        for i in ans:
            lits = list()
            lits.append(self.pos(i))
            lits.append(self.neg(lit))
            self.lcnf(lits)
        
        lits = list()
        for i in ans:
            lits.append(self.neg(i))
        lits.append(self.pos(lit))
        self.lcnf(lits)

        return lit

    def lor_list(self, params):
        # degenerate when size = 0, 1, 2
        if(len(params)==0): return self.const_literal(False)
        if(len(params)==1): return params[0]
        if(len(params)==2): return self.lor(params[0], params[1])

        for i in params:
            if(self.is_true(i)): return self.const_literal(True)
        
        ans = self.eliminate_duplicates(params)
        lit = self.make_literal()

        for i in ans:
            lits = list()
            lits.append(self.neg(i))
            lits.append(self.pos(lit))
            self.lcnf(lits)
        
        lits = list()
        for i in ans:
            lits.append(self.pos(i))
        lits.append(self.neg(lit))
        self.lcnf(lits)

        return lit

    def lxor_list(self, params):
        # degenerate when size = 0, 1, 2
        if(len(params)==0): return self.const_literal(False)
        if(len(params)==1): return params[0]
        if(len(params)==2): return self.lxor(params[0], params[1])

        lit=self.const_literal(False) 

        for i in params:
            lit = self.lxor(i, lit)

        return lit
    
    def eliminate_duplicates(self, params):
        ans = []
        for i in params:
            if(i not in ans):
                ans.append(i)
        return ans


    # internal function of AND, OR, XOR, NAND, NOR, EQ, IMPLY 
    def _internal_land(self, a, b, o):
        ans = list()
        ans.append(self.pos(a))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(b))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.neg(a))
        ans.append(self.neg(b))
        ans.append(self.pos(o))
        self.lcnf(ans)
        
    def _internal_lor(self, a, b, o):
        ans = list()
        ans.append(self.neg(a))
        ans.append(self.pos(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.neg(b))
        ans.append(self.pos(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(a))
        ans.append(self.pos(b))
        ans.append(self.neg(o))
        self.lcnf(ans)
        
    def _internal_lxor(self, a, b, o):
        ans = list()
        ans.append(self.neg(a))
        ans.append(self.neg(b))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(a))
        ans.append(self.pos(b))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.neg(a))
        ans.append(self.pos(b))
        ans.append(self.pos(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(a))
        ans.append(self.neg(b))
        ans.append(self.pos(o))
        self.lcnf(ans)

    def _internal_lnand(self, a, b, o):
        ans = list()
        ans.append(self.pos(a))
        ans.append(self.pos(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(b))
        ans.append(self.pos(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.neg(a))
        ans.append(self.neg(b))
        ans.append(self.neg(o))
        self.lcnf(ans)

    def _internal_lnor(self, a, b, o):
        ans = list()
        ans.append(self.neg(a))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.neg(b))
        ans.append(self.neg(o))
        self.lcnf(ans)

        ans = list()
        ans.append(self.pos(a))
        ans.append(self.pos(b))
        ans.append(self.pos(o))
        self.lcnf(ans)

    def _internal_lequal(self, a, b, o):
        self._internal_lxor(a, b, self.lnot(o))

    def _internal_limplies(self, a, b, o):
        self._internal_lor(self.lnot(a), b, o)

    def is_true(self, lit):
        return lit==-1

    def is_false(self, lit):
        return lit==0

    def const_literal(self, val):
        if(val): return literal(-1)
        else: return literal(0)