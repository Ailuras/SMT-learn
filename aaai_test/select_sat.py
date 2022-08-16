import os
import shutil


# 分类的函数
def classify(path='', max_time='none', min_time='none'):
    if max_time == 'none':
        target_path = path
        max_time = 1250000
    else:
        target_path = path + '_max' + max_time
        max_time = int(max_time)*1000
    if min_time == 'none':
        min_time = 0
    else:
        target_path = target_path + '_min' + min_time
        min_time = int(max_time)*1000
    target_path = target_path + '_classify'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    elif os.path.exists(target_path):
        shutil.rmtree(target_path)
        # return
        os.makedirs(target_path)
    # shutil.copytree(path, target_path)
    # os.makedirs(target_path + '')
    file = open(target_path + '/AProVE.log','w')
    file.close()
    file = open(target_path + '/calypto.log','w')
    file.close()
    file = open(target_path + '/Dartagnan.log','w')
    file.close() 
    file = open(target_path + '/LassoRanker.log','w')
    file.close() 
    file = open(target_path + '/leipzig.log','w')
    file.close() 
    file = open(target_path + '/mcm.log','w')
    file.close() 
    file = open(target_path + '/CInteger.log','w')
    file.close()
    file = open(target_path + '/ITS.log','w')
    file.close() 
    file = open(target_path + '/SAT14.log','w')
    file.close() 
    file = open(target_path + '/MathProblems.log','w')
    file.close() 

    # os.makedirs(target_path + '/aprove')
    # os.makedirs(target_path + '/calypto')
    # os.makedirs(target_path + '/dartagnan')
    # os.makedirs(target_path + '/lassoranker')
    # os.makedirs(target_path + '/leipzig')
    # os.makedirs(target_path + '/mcm')
    # os.makedirs(target_path + '/cinteger_its_sat14')
    # os.makedirs(target_path + '/mathproblems')
    
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
                        run_time = int(line.split(' : ')[1][:-4])
                        if "AProVE" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/AProVE.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "calypto" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/calypto.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "Dartagnan" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/Dartagnan.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "LassoRanker" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/LassoRanker.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "leipzig" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/leipzig.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "mcm" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/mcm.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "CInteger" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/CInteger.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "ITS" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/ITS.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "SAT14" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/SAT14.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "MathProblems" in line and run_time <= max_time and run_time >= min_time:
                            with open(target_path + '/MathProblems.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        info.clear()

# 获取全都解出来的例子

def get_sat(path='blan'):
    sat_list = []
    if os.path.exists('error.log'):
        os.remove('error.log')
    
    file_list = os.listdir(path)
    if path == 'blan':
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
                    if result == 'sat':
                        sat_list.append(info.split(' : ')[0])
                    elif result == 'timeout':
                        continue
                    else:
                        with open('error.log',"a") as f1:
                            f1.write(new_path, info)
    print(path, 'sat: ', len(sat_list))
    # print(sat_list[0])
    select(path, sat_list)

def get_all_sat(path='blan', all_sat_list=[]):
    if os.path.exists('error.log'):
        os.remove('error.log')
    
    file_list = os.listdir(path)
    if path == 'blan':
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
                        all_sat_list.append(info.split(' : ')[0])
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
                        if info.split(' : ')[0] in all_sat_list:
                            all_sat_list.remove(info.split(' : ')[0])
                    elif result == 'sat':
                        if info.split(' : ')[0] in all_sat_list:
                            if int(info.split(' : ')[1][:-4]) > 1250000:
                                all_sat_list.remove(info.split(' : ')[0])
                    else:
                        with open('error.log',"a") as f1:
                            f1.write(new_path, info)
    print(path, 'all_sat: ', len(all_sat_list))
    return all_sat_list
    # print(sat_list[0])

def select(path='blan', sat_list=[], flag=True):
    if flag == True:
        target_path = path + '_sat'
    else:
        target_path = path + '_all_sat'
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

# all_sat_list = []

# get_all_sat()
# get_all_sat(path='cvc5')
# get_all_sat(path='z3')
# get_all_sat(path='mathsat')
# get_all_sat(path='z3(b)')
# get_all_sat(path='yices2')
# get_all_sat(path='aprove')

# # with open('allsat.log',"w") as f:
# #     for i in all_sat_list:
# #         f.write(i+'\n')

# select(sat_list=all_sat_list, flag=False)
# select(path='cvc5', sat_list=all_sat_list, flag=False)
# select(path='z3', sat_list=all_sat_list, flag=False)
# select(path='mathsat', sat_list=all_sat_list, flag=False)
# select(path='z3(b)', sat_list=all_sat_list, flag=False)
# select(path='yices2', sat_list=all_sat_list, flag=False)
# select(path='aprove', sat_list=all_sat_list, flag=False)

# classify('blan_all_sat', 'none', 'none')
# classify('z3_all_sat', 'none', 'none')
# classify('z3(b)_all_sat', 'none', 'none')
# classify('cvc5_all_sat', 'none', 'none')
# classify('aprove_all_sat', 'none', 'none')
# classify('yices2_all_sat', 'none', 'none')
# classify('mathsat_all_sat', 'none', 'none')


# get_sat(path='diffc/4')
# get_sat(path='diffc/8')
# get_sat(path='diffc/16')
# get_sat(path='diffc/24')
# get_sat(path='diffc/32')
# select(path='diffc/4')
# select(path='diffc/8')
# select(path='diffc/16')
# select(path='diffc/24')
# select(path='diffc/32')