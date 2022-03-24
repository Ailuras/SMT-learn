from SMTSolver import SMTS
from examples.examples_list import examples

import z3
import time

if(__name__=="__main__"):
    answer = []
    ex = examples()
    test_list = ex.all()
    for i in test_list:
        print("---------"+i+":---------")
        time1 = time.clock()
        smt_solver = SMTS()
        smt_solver.parse(i)
        time1 = time.clock() - time1

        time2 = time.clock()
        z3_solver = z3.Solver()
        z3_solver.from_file(i)
        ans = z3_solver.check()
        print(ans)
        # if(str(ans)=="sat"): print(z3_solver.model())
        time2 = time.clock() - time2

        print(str(time1)+" "+str(time2))
        answer.append((time1, time2))
        
        print()

    # for i in answer:
    #     print(str(i[0])+" "+str(i[1]))
    # print(answer)

