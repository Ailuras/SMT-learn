import pandas as pd
import os
import shutil
import sys

def classify(path='', time='none'):
    if time == 'none':
        time = 10000000
        target_path = path + '_classify'
    else:
        target_path = path + '_classify_' + time
        time = int(time)*1000
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    elif os.path.exists(target_path):
        shutil.rmtree(target_path)
        return
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
                        if "AProVE" in line and run_time <= time:
                            with open(target_path + '/AProVE.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "calypto" in line and run_time <= time:
                            with open(target_path + '/calypto.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "Dartagnan" in line and run_time <= time:
                            with open(target_path + '/Dartagnan.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "LassoRanker" in line and run_time <= time:
                            with open(target_path + '/LassoRanker.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "leipzig" in line and run_time <= time:
                            with open(target_path + '/leipzig.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "mcm" in line and run_time <= time:
                            with open(target_path + '/mcm.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "CInteger" in line and run_time <= time:
                            with open(target_path + '/CInteger.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "ITS" in line and run_time <= time:
                            with open(target_path + '/ITS.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "SAT14" in line and run_time <= time:
                            with open(target_path + '/SAT14.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "MathProblems" in line and run_time <= time:
                            with open(target_path + '/MathProblems.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        info.clear()


# classify('hhh')
# classify('z3')
# classify('z3(b)')
# classify('cvc5')
# classify('aprove')
# classify('yices2')
# classify('mathsat')

a = '10'
classify('hhh', a)
classify('z3', a)
classify('z3(b)', a)
classify('cvc5', a)
classify('aprove', a)
classify('yices2', a)
classify('mathsat', a)
