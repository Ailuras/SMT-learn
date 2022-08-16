import pandas as pd
import os
import shutil
import sys

from select_sat import classify, get_all_sat, get_sat, select

a = sys.argv[2]
b = sys.argv[1]

# classify('blan_4', max_time=a, min_time=b)
# classify('blan_8', max_time=a, min_time=b)
# classify('blan_16', max_time=a, min_time=b)
# classify('blan_24', max_time=a, min_time=b)
# classify('blan_32', max_time=a, min_time=b)
# classify('blan(p)', max_time=a, min_time=b)
classify('blan', max_time=a, min_time=b)
classify('z3', max_time=a, min_time=b)
classify('z3(b)', max_time=a, min_time=b)
classify('cvc5', max_time=a, min_time=b)
classify('aprove', max_time=a, min_time=b)
classify('yices2', max_time=a, min_time=b)
classify('mathsat', max_time=a, min_time=b)

# get_sat()
# get_sat(path='blan_4')
# get_sat(path='blan_8')
# get_sat(path='blan_16')
# get_sat(path='blan_24')
# get_sat(path='blan_32')

all_sat_list = []

# all_sat_list = get_all_sat(path='blan_4', all_sat_list=all_sat_list)
# all_sat_list = get_all_sat(path='blan_8', all_sat_list=all_sat_list)
# all_sat_list = get_all_sat(path='blan_16', all_sat_list=all_sat_list)
# all_sat_list = get_all_sat(path='blan_24', all_sat_list=all_sat_list)
# all_sat_list = get_all_sat(path='blan_32', all_sat_list=all_sat_list)
# all_sat_list = get_all_sat(path='blan(p)', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='cvc5', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='z3', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='mathsat', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='z3(b)', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='yices2', all_sat_list=all_sat_list)
all_sat_list = get_all_sat(path='aprove', all_sat_list=all_sat_list)

# select(path='blan_4', sat_list=all_sat_list, flag=False)
# select(path='blan_8', sat_list=all_sat_list, flag=False)
# select(path='blan_16', sat_list=all_sat_list, flag=False)
# select(path='blan_24', sat_list=all_sat_list, flag=False)
# select(path='blan_32', sat_list=all_sat_list, flag=False)
# select(path='blan(p)', sat_list=all_sat_list, flag=False)

select(sat_list=all_sat_list, flag=False)
select(path='cvc5', sat_list=all_sat_list, flag=False)
select(path='z3', sat_list=all_sat_list, flag=False)
select(path='mathsat', sat_list=all_sat_list, flag=False)
select(path='z3(b)', sat_list=all_sat_list, flag=False)
select(path='yices2', sat_list=all_sat_list, flag=False)
select(path='aprove', sat_list=all_sat_list, flag=False)

# classify('blan(p)_all_sat', 'none', 'none')
classify('blan_all_sat', 'none', 'none')
classify('z3_all_sat', 'none', 'none')
classify('z3(b)_all_sat', 'none', 'none')
classify('cvc5_all_sat', 'none', 'none')
classify('aprove_all_sat', 'none', 'none')
classify('yices2_all_sat', 'none', 'none')
classify('mathsat_all_sat', 'none', 'none')