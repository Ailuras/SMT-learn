import os
import shutil

all_sat_list = []

nums = 0
index = 0
file_list = os.listdir('blan_all_sat_classify')
for file in file_list:
    new_path = os.path.join('blan_all_sat_classify', file)
    with open(new_path) as f:
        lines = f.readlines()
        for line in lines:
            if 'Number of variables' in line:
                nums += 1
            if 'SAT_Split_100' in line:
                index += 1
print(index)
print('blan: ', nums/index)
                
nums = 0
index = 0
file_list = os.listdir('blan(p)_all_sat_classify')
for file in file_list:
    new_path = os.path.join('blan(p)_all_sat_classify', file)
    with open(new_path) as f:
        lines = f.readlines()
        for line in lines:
            if 'Number of variables' in line:
                nums += 1
            if 'SAT_Split_100' in line:
                index += 1
print(index)
print('blan(p): ', nums/index)