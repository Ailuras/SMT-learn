
from copy import deepcopy
from smtlib.Parser import SmtlibParser
from solver.smt_solver import smt_solver_s

import argparse
parser = argparse.ArgumentParser(description="SMT Solver")

parser.add_argument('-f','--file',dest='file',metavar='N')

class SMTS(object):
    def __init__(self, *options):
        self.parser = SmtlibParser()

    def parse(self, file):
        self.parser.parse(file)

if(__name__=="__main__"):
    SMTSolver = SMTS()
    args = parser.parse_args()
    if(args.file != ""):
        SMTSolver.solve(args.file)

