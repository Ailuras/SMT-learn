import os
import shutil

def get_sat(path='hhh'):
    if os.path.exists('error.log'):
        os.remove('error.log')
    
    file_list = os.listdir(path)
    if path == 'hhh':
        for file in file_list:
            new_path = os.path.join(path, file)
            with open(new_path) as f:
                while f.readline():
                    info = f.readline()
                    result = 'timeout'
                    while info[:3] != 'SAT' and info:
                        result = info[:-1]
                        info = f.readline()
                    if result[:3] == 'che':
                        sat_list.append(info.split(' : ')[0])
                    elif result[:3] == 'com':
                        continue
                    else:
                        with open('error.log',"a") as f1:
                            f1.write(info)
    else:
        for file in file_list:
            new_path = os.path.join(path, file)
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
                    if result == 'timeout':
                        if info.split(' : ')[0] in sat_list:
                            sat_list.remove(info.split(' : ')[0])
                    elif result == 'sat':
                        continue
                    else:
                        with open('error.log',"a") as f1:
                            f1.write(new_path, info)
    print(len(sat_list))
    # print(sat_list[0])

def select(path='hhh'):
    target_path = path + '_sat'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    elif os.path.exists(target_path):
        shutil.rmtree(target_path)
        # return
        os.makedirs(target_path)
    file = open(target_path + '/sat.log','w')
    file.close()
    
    file_list = os.listdir(path)
    for file in file_list:
        new_path = os.path.join(path, file)
        if not os.path.isdir(new_path):
            with open(new_path) as f:
                lines = f.readlines()
                info = []
                for line in lines:
                    if 'SAT_Split_100' not in line:
                        info.append(line)
                    else:
                        info.append(line)
                        if line.split(' : ')[0] in sat_list:
                            with open(target_path + '/sat.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        info.clear()

    
sat_list = []

get_sat()
get_sat(path='cvc5')
get_sat(path='z3')
get_sat(path='mathsat')
get_sat(path='z3(b)')
get_sat(path='yices2')
get_sat(path='aprove')

select()
select(path='cvc5')
select(path='z3')
select(path='mathsat')
select(path='z3(b)')
select(path='yices2')
select(path='aprove')
