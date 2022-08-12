import pandas as pd
import os
import os
import shutil
from tqdm import tqdm
import matplotlib.pyplot as plt


def classify(path=''):
    target_path = path + '_after'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    # shutil.copytree(path, target_path)
    os.makedirs(target_path + '/new')
    file = open(target_path + '/new/AProVE.log','w')
    file.close()
    file = open(target_path + '/new/calypto.log','w')
    file.close()
    file = open(target_path + '/new/Dartagnan.log','w')
    file.close() 
    file = open(target_path + '/new/LassoRanker.log','w')
    file.close() 
    file = open(target_path + '/new/leipzig.log','w')
    file.close() 
    file = open(target_path + '/new/mcm.log','w')
    file.close() 
    file = open(target_path + '/new/CInteger_ITS_SAT14.log','w')
    file.close() 
    file = open(target_path + '/new/MathProblems.log','w')
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
                        if "AProVE" in line:
                            with open(target_path + '/new/AProVE.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "calypto" in line:
                            with open(target_path + '/new/calypto.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "Dartagnan" in line:
                            with open(target_path + '/new/Dartagnan.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "LassoRanker" in line:
                            with open(target_path + '/new/LassoRanker.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "leipzig" in line:
                            with open(target_path + '/new/leipzig.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "mcm" in line:
                            with open(target_path + '/new/mcm.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "CInteger" in line or "ITS" in line or "SAT14" in line:
                            with open(target_path + '/new/CInteger_ITS_SAT14.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        elif "MathProblems" in line:
                            with open(target_path + '/new/MathProblems.log',"a") as f:
                                for i in info:
                                    f.write(i)
                        info.clear()

classify('z3')
