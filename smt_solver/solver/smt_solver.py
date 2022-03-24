# from solver.dpllt import dpllt_solver_s
from solver.dpllt import dpllt_solver_s
import sys

# options setting, total here!
def options_init():
    return {
        "authors": "Fuqi Jia",
        "name": "berry",
        "version": "1.0.0",
        "error_behavior": "immediate-exit",
        # "immediate-exit" or "continued-execution"
        "reason_unknown": "???",

        # static variable
        "current_mode": 0,
        # 0-start mode; 1-assert mode; 2-sat mode; 3-unsat mode
        "logic_name": "",

        "theory_solver_reset": False,

        # options
        "regular_output_channel": "stdout",
        "diagnostic_output_channel": "stderr",
        "global_declarations": False,
        "print_success": True,
        "produce_assertions": False,
        "produce_models": False,
        "produce_proofs": False,
        "produce_unsat_assumptions": False,
        "produce_unsat_cores": False,
        "random_seed": 0,
        "reproducible_resource_limit": 0,
        "verbosity": 0
    }

class smt_solver_s(dpllt_solver_s):
    def __init__(self):
        super(smt_solver_s, self).__init__()
        self.options = options_init()

        self.logic_support=["QF_LRA"] # support logic solver: simplex(int, real), sat

        # now, in declaring, when defined to add_xxx {"name": arity}
        self.declaring_sorts=dict()

    def sys_print(self, dir, val):
        val = val + "\n"
        if(dir=="stdout"):
            sys.stdout.write(val)
        elif(dir=="stderr"):
            sys.stderr.write(val)
        else:
            with open(dir,"a") as f:
                f.write(val)

    def regular_output(self, val):
        self.sys_print(self.options["regular_output_channel"], val)
    
    def diagnostic_output(self, val):
        self.sys_print(self.options["diagnostic_output_channel"], val)

    def echo(self, val):
        self.regular_output(val)

    def exit(self):
        # sys.exit(0)
        pass

    def get_info(self, key):
        if(key=="all-statistics"):
            pass
        elif(key=="assertion-stack-levels"):
            self.regular_output("(:assertion-stack-levels " + str(self.options["assertion_stack_levels"]) + ")")
        elif(key=="authors"):
            self.regular_output("(:authors " + self.options["authors"] + ")")
        elif(key=="error-behavior"):
            self.regular_output("(:error-behavior " + self.options["error_behavior"] + ")")
        elif(key=="name"):
            self.regular_output("(:name " + self.options["name"] + ")")
        elif(key=="reason-unknown"):
            self.regular_output("(:reason-unknown " + self.options["reason_unknown"] + ")")
        elif(key=="version"):
            self.regular_output("(:versioin " + self.options["version"] + ")")
        else:
            #self.regular_output("error info-flag")
            self.diagnostic_output("get-info has error!")

    def Assert(self, assertions):
        self.add_assertion(assertions)
    
    def get_option(self, keyword):
        pass

    def get_model(self):
        answer = self.get_answer()
        self.regular_output(answer)

    def set_info(self, key, val):
        if(key=="error-behavior"):
            self.options["error-behavior"] = val
        else:
            self.options[key] = val
            #self.regular_output("error info-flag")
            # self.diagnostic_output("set-info has error!")

    def set_logic(self, symbol):
        # if(self.options["current_mode"]==1):
        #     self.diagnostic_output("the logic had been set!")
        #     self.exit()
        self.setLogic(symbol)
        
        # cannot set all
        if(symbol in self.logic_support):
            self.options["logic_name"] = symbol
            self.setLogic(symbol) # set super's theory solver
            self.options["current_mode"] = 1 # assert mode

    def str2bool(self, val):
        if(val.lower()=="true"):
            return True
        else:
            return False

    def set_option(self, key, val):
        if(key=="diagnostic-output-channel"):
            self.options["diagnostic_output_channel"] = val
        elif(key=="global-declarations"):
            self.options["global_declarations"] = self.str2bool(val)
        elif(key=="interactive-mode"):
            self.diagnostic_output("using :produce-assertions instead!")
        elif(key=="print-success"):
            self.options["print_success"] = self.str2bool(val)
        elif(key=="produce-assertions"):
            self.options["produce_assertions"] = self.str2bool(val)
        elif(key=="produce-assignments"):
            self.options["produce_assignments"] = self.str2bool(val)
        elif(key=="produce-models"):
            self.options["produce_models"] = self.str2bool(val)
        elif(key=="produce-proofs"):
            self.options["produce_proofs"] = self.str2bool(val)
        elif(key=="produce-unsat-assumptions"):
            self.options["produce_unsat_assumptions"] = self.str2bool(val)
        elif(key=="produce-unsat-cores"):
            self.options["produce_unsat_cores"] = self.str2bool(val)
        elif(key=="random-seed"):
            self.options["random_seed"] = int(val)
        elif(key=="regular-output-channel"):
            self.options["regular_output_channel"] = val
        elif(key=="reproducible-resource-limit"):
            self.options["reproducible_resource_limit"] = int(val)
        elif(key=="verbosity"):
            self.options["verbosity"] = int(val)
        else:
            self.diagnostic_output("set-info")

    def reset(self):
        pass

    def check_sat(self):
        ans = self.solve()
        # if(ans): self.regular_output("sat, solving time: %s"%(str(round(self.time, 5)) + "s"))
        # else: self.regular_output("unsat, solving time: %s"%(str(round(self.time, 5)) + "s"))
        if(ans): self.regular_output("sat")
        else: self.regular_output("unsat")
        return ans

    def check_sat_assuming(self, assumptions):
        return self.solve(assumptions)

    def get_proof(self):
        print("get-proof")

    def get_unsat_assumptions(self):
        print("get-unsat-assumptions")
    
    def get_unsat_core(self):
        print("get-unsat-core")

    def get_assertions(self):
        print("get-assertions")
    
    def get_assignment(self):
        print("get-assignment")

    def declare_const(self, symbol, sort):
        return self.add_variable(symbol, sort)
        
    def declare_datatype(self, symbol, datatype_dec):
        self.diagnostic_output("declare-datatype is now not supported!")
        pass

    def declare_datatypes(self, sort_dec_list, datatype_dec_list):
        self.diagnostic_output("declare-datatypes is now not supported!")
        pass

    def declare_fun(self, symbol, in_sort_list, out_sort):
        if(len(in_sort_list)==0):
            self.declare_const(symbol, out_sort)
        else:
            raise NotImplementedError()
    
    def declare_sort(self, symbol, numeral):
        pass

    def define_fun(self, function_def):
        self.diagnostic_output("define-fun")
        pass

    def define_fun_rec(self, funtion_def):
        self.diagnostic_output("define-fun-rec")
        pass
    
    def define_funs_rec(self, function_def_list, term_list):
        self.diagnostic_output("define-funs-rec")
        pass

    def define_sort(self, sym, symbol_list, sor):
        self.diagnostic_output("define-sort")
        pass
        # self.add_sort(sym, symbol_list, self.declaring_sorts[sym], sor)
    
if(__name__=="__main__"):
    s = smt_solver_s()