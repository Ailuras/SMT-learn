import smtlib.Commands as smtcmd

class SmtlibCommand(object):
    def __init__(self, smt_sovler, name, args=None):
        self.smt_sovler = smt_sovler
        self.name = name
        self.args = args

    def __call__(self):
        if(self.name == smtcmd.SET_OPTION):
            assert(len(self.args)>=1)
            return self.smt_sovler.set_option(self.args[0])
        elif(self.name == smtcmd.SET_INFO):
            assert(len(self.args)>=2)
            return self.smt_sovler.set_info(self.args[0], self.args[1])
        elif(self.name == smtcmd.SET_LOGIC):
            assert(len(self.args)>=1)
            return self.smt_sovler.set_logic(self.args[0])
        elif(self.name == smtcmd.CHECK_SAT):
            return self.smt_solver.check_sat()
        elif(self.name == smtcmd.ASSERT):
            assert(len(self.args)>=1)
            return self.smt_sovler.Assert(self.args[0])
        elif(self.name == smtcmd.CHECK_SAT_ASSUMING):
            assert(len(self.args)>=1)
            return self.smt_sovler.check_sat_assuming(self.args[0])
        elif(self.name == smtcmd.DECLARE_CONST):
            assert(len(self.args)>=2)
            return self.smt_sovler.declare_const(self.args[0], self.args[1])
        elif(self.name == smtcmd.DECLARE_DATATYPE):
            assert(len(self.args)>=2)
            return self.smt_sovler.declare_datatype(self.args[0], self.args[1])
        elif(self.name == smtcmd.DECLARE_DATATYPES):
            assert(len(self.args)>=2)
            return self.smt_sovler.declare_datatypes(self.args[0], self.args[1])
        elif(self.name == smtcmd.DECLARE_FUN):
            assert(len(self.args)>=3)
            return self.smt_sovler.declare_fun(self.args[0], self.args[1], self.args[2])
        elif(self.name == smtcmd.DECLARE_SORT):
            assert(len(self.args)>=2)
            return self.smt_sovler.declare_sort(self.args[0], self.args[1])
        elif(self.name == smtcmd.DEFINE_FUN):
            assert(len(self.args)>=1)
            return self.smt_sovler.define_fun(self.args[0])
        elif(self.name == smtcmd.DEFINE_FUN_REC):
            assert(len(self.args)>=1)
            return self.smt_sovler.define_fun_rec(self.args[0])
        elif(self.name == smtcmd.DEFINE_FUN_RECS):
            assert(len(self.args)>=2)
            return self.smt_sovler.define_fun_recs(self.args[0], self.args[1])
        elif(self.name == smtcmd.DEFINE_SORT):
            assert(len(self.args)>=3)
            return self.smt_sovler.define_fun(self.args[0],self.args[1],self.args[2])
        elif(self.name == smtcmd.ECHO):
            assert(len(self.args)>=1)
            return self.smt_solver.echo(self.args[0])
        elif(self.name == smtcmd.EXIT):
            return self.smt_sovler.exit()
        elif(self.name == smtcmd.GET_ASSERTIONS):
            return self.smt_sovler.get_assertions()
        elif(self.name == smtcmd.GET_ASSIGNMENT):
            return self.smt_sovler.get_assignment()
        elif(self.name == smtcmd.GET_INFO):
            assert(len(self.args)>=1)
            return self.smt_sovler.get_info(self.args[0])
        elif(self.name == smtcmd.GET_MODEL):
            return self.smt_sovler.get_model()
        elif(self.name == smtcmd.GET_OPTION):
            assert(len(self.args)>=1)
            return self.smt_sovler.get_option(self.args[0])
        elif(self.name == smtcmd.GET_PROOF):
            return self.smt_sovler.get_proof()
        elif(self.name == smtcmd.GET_UNSAT_ASSUMPTIONS):
            return self.smt_sovler.get_unsat_assumptions()
        elif(self.name == smtcmd.GET_UNSAT_CORE):
            return self.smt_sovler.get_unsat_core()
        elif(self.name == smtcmd.GET_VALUE):
            assert(len(self.args)>=1)
            return self.smt_sovler.get_value(self.args[0])
        elif(self.name == smtcmd.POP):
            assert(len(self.args)>=1)
            return self.smt_sovler.pop(self.args[0])
        elif(self.name == smtcmd.PUSH):
            assert(len(self.args)>=1)
            return self.smt_sovler.push(self.args[0])
        elif(self.name == smtcmd.RESET):
            return self.smt_sovler.reset()
        elif(self.name == smtcmd.RESET_ASSERTIONS):
            return self.smt_sovler.reset_assertions()

    def __str__(self):
        ans = "("
        ans += self.name
        for i in self.args:
            ans += (" " + str(i))
        ans += ")"
        return ans


class SmtlibScript(object):
    def __init__(self):
        self.CommandStack = []
        # self.annotations = None
        self.logic = None
    
    def append(self, cmd):
        self.CommandStack.append(cmd)

    def run(self):
        for i in self.CommandStack:
            i()
