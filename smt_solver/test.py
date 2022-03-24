from SMTSolver import SMTS
from examples.examples_list import examples

import z3
import time

if(__name__=="__main__"):
    dtp = "./examples/DTP-Scheduling/constraints-cooking09.smt2"
    test = "./examples/test/test9.smt2"
    smt_solver = SMTS()
    smt_solver.parse(dtp)