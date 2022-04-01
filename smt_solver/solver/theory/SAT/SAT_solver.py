#encoding:utf-8
import os
import sys

# 返回当前工作目录
path = os.getcwd()
pl = path.split("\\", -1)

if(pl[-1]=="SAT"):
    # in folder of QF_LRA
    from cdcl import cdcl_solver_s
else:
    # in folder of SMT_Solver
    from cdcl import cdcl_solver_s

class solver(cdcl_solver_s):
    pass

if(__name__=="__main__"):
    s = solver()
    s.parse("smt_solver/solver/theory/SAT/test.cnf")
    print(s.solve())
    print(s.get_model())