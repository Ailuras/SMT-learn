import pandas as pd
import os
import shutil
import sys

from select_sat import classify

a = sys.argv[2]
b = sys.argv[1]

classify('hhh', max_time=a, min_time=b)
# classify('hhh(p)', max_time=a, min_time=b)

classify('z3', max_time=a, min_time=b)
classify('z3(b)', max_time=a, min_time=b)
classify('cvc5', max_time=a, min_time=b)
classify('aprove', max_time=a, min_time=b)
classify('yices2', max_time=a, min_time=b)
classify('mathsat', max_time=a, min_time=b)