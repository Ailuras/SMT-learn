import pandas as pd
import os
import shutil
import sys

from select_sat import classify, get_all_sat, select

a = sys.argv[2]
b = sys.argv[1]

classify('blan', max_time=a, min_time=b)
# classify('hhh(p)', max_time=a, min_time=b)
classify('z3', max_time=a, min_time=b)
classify('z3(b)', max_time=a, min_time=b)
classify('cvc5', max_time=a, min_time=b)
classify('aprove', max_time=a, min_time=b)
classify('yices2', max_time=a, min_time=b)
classify('mathsat', max_time=a, min_time=b)

all_sat_list = []

all_sat_list = get_all_sat(all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='cvc5', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='z3', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='mathsat', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='z3(b)', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='yices2', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='aprove', all_sat_list=all_sat_list)

select(sat_list=all_sat_list, flag=False)
select(path='cvc5', sat_list=all_sat_list, flag=False)
select(path='z3', sat_list=all_sat_list, flag=False)
select(path='mathsat', sat_list=all_sat_list, flag=False)
select(path='z3(b)', sat_list=all_sat_list, flag=False)
select(path='yices2', sat_list=all_sat_list, flag=False)
select(path='aprove', sat_list=all_sat_list, flag=False)

classify('blan_all_sat', 'none', 'none')
classify('z3_all_sat', 'none', 'none')
classify('z3(b)_all_sat', 'none', 'none')
classify('cvc5_all_sat', 'none', 'none')
classify('aprove_all_sat', 'none', 'none')
classify('yices2_all_sat', 'none', 'none')
classify('mathsat_all_sat', 'none', 'none')