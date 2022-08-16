import os
import shutil

all_sat_list = []

new_path = os.path.join('blan_all_sat_classify/ITS.log')
with open(new_path) as f:
    while f.readline():
        info = f.readline()
        result = 'timeout'
        while info[:3] != 'SAT' and info:
            result = info[:-1]
            info = f.readline()
        if result[:3] == 'che':
            all_sat_list.append(info.split(' : ')[0])
        elif result[:3] == 'com':
            continue
        else:
            with open('error.log',"a") as f1:
                f1.write(info)


new_path = os.path.join('cvc5_all_sat_classify/ITS.log')
with open(new_path) as f:
    while f.readline():
        info = f.readline()
        result = 'timeout'
        while info[:3] != 'SAT' and info:
            if info[:3] == 'com' or info[:3] == 'unk' or info[:3] == 'tim':
                result = 'timeout'
            if info[:3] == 'sat':
                result = 'sat'
            info = f.readline()
        if result == 'sat':
            if info.split(' : ')[0] in all_sat_list:
                all_sat_list.remove(info.split(' : ')[0])
        elif result == 'timeout':
            continue
        else:
            with open('error.log',"a") as f1:
                f1.write(new_path, info)


print('count: ', len(all_sat_list))
print(all_sat_list)