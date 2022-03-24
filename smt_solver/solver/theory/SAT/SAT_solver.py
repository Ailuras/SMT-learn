import os
import sys

path = os.getcwd()
pl = path.split("\\",-1)

if(pl[-1]=="SAT"):
    # in folder of QF_LRA
    from cdcl import cdcl_solver_s
else:
    # in folder of SMT_Solver
    from solver.theory.SAT.cdcl import cdcl_solver_s

class solver(cdcl_solver_s):
    pass

if(__name__=="__main__"):
    s = solver()
    s.parse("./test3.cnf")
    print(s.solve())
    print(s.get_model())