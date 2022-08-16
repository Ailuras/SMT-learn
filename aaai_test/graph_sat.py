from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

from get_data import get_data, get_data_new
from select_sat import get_sat, select, classify

instances_aprove = []
time_aprove = []
instances_cvc5 = []
time_cvc5 = []
instances_ours = []
time_ours = []
instances_yices = []
time_yices = []
instances_z3 = []
time_z3 = []
instances_cvc5b = []
time_cvc5b = []
instances_z3b = []
time_z3b= []

def get_graph_sat(category='none', graph='none'):
    
    # 生成数据
    if category == 'none':
        if graph == 'none':
            instances_aprove, time_aprove = get_data('./aprove_all_sat_classify/', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data('./cvc5_all_sat_classify/', 'SAT_Split_100')
            instances_ours, time_ours = get_data('./blan_all_sat_classify/', 'SAT_Split_100')
            instances_yices, time_yices = get_data('./yices2_all_sat_classify/', 'SAT_Split_100')
            instances_z3, time_z3 = get_data('./z3_all_sat_classify/', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data('./mathsat_all_sat_classify/', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data('./z3(b)_all_sat_classify/', 'SAT_Split_100')
        else:
            instances_aprove, time_aprove = get_data_new('./aprove_sat_classify/', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data_new('./cvc5_sat_classify/', 'SAT_Split_100')
            instances_ours, time_ours = get_data_new('./blan_sat_classify/', 'SAT_Split_100')
            instances_yices, time_yices = get_data_new('./yices2_sat_classify/', 'SAT_Split_100')
            instances_z3, time_z3 = get_data_new('./z3_sat_classify/', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data_new('./mathsat_sat_classify/', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data_new('./z3(b)_sat_classify/', 'SAT_Split_100')

    else:
        if graph == 'none':
            instances_aprove, time_aprove = get_data('./aprove_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data('./cvc5_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_ours, time_ours = get_data('./blan_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_yices, time_yices = get_data('./yices2_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3, time_z3 = get_data('./z3_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data('./mathsat_all_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data('./z3(b)_all_sat_classify/'+category+'.log', 'SAT_Split_100')
        else:
            instances_aprove, time_aprove = get_data_new('./aprove_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data_new('./cvc5_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_ours, time_ours = get_data_new('./blan_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_yices, time_yices = get_data_new('./yices2_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3, time_z3 = get_data_new('./z3_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data_new('./mathsat_sat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data_new('./z3(b)_sat_classify/'+category+'.log', 'SAT_Split_100')

    # print('time_aprove  : ', time_aprove[-1])
    # print('time_cvc5    : ', time_cvc5[-1])
    # print('time_blan     : ', time_ours[-1])
    # print('time_yices   : ', time_yices[-1])
    # print('time_z3      : ', time_z3[-1])
    # print('time_mathsat : ', time_cvc5b[-1])
    # print('time_z3b     : ', time_z3b[-1])
    
    # 生成图形
    plt.plot(instances_aprove, time_aprove, 'blue', label='APROVE')
    plt.plot(instances_cvc5, time_cvc5, 'green', label='CVC5')
    plt.plot(instances_cvc5b, time_cvc5b, 'orange', label='MATHSAT')
    plt.plot(instances_yices, time_yices, 'gold', label='YICES2')
    plt.plot(instances_z3, time_z3, 'violet', label='Z3')
    plt.plot(instances_z3b, time_z3b, 'lawngreen', label='Z3(B)')
    plt.plot(instances_ours, time_ours, 'r', label='BLAN')

    if graph == 'none':
        plt.ylabel('TIME (S)') # 横坐标轴的标题
        plt.xlabel('INSTANCES') # 纵坐标轴的标题
    else:
        plt.ylabel('cumulative score') # 横坐标轴的标题
        plt.xlabel('time (s)') # 纵坐标轴的标题
    plt.legend() # 显示图例, 图例中内容由 label 定义
    plt.yscale("log")
    # plt.xscale("log")
    if category == 'none':
        plt.savefig('result/experiments_sat.pdf')
    else:
        plt.savefig('result/experiments_sat_' + category + '.pdf')
    # plt.show()
    plt.close()

# get_sat()
# get_sat(path='cvc5')
# get_sat(path='z3')
# get_sat(path='mathsat')
# get_sat(path='z3(b)')
# get_sat(path='yices2')
# get_sat(path='aprove')

# select()
# select(path='cvc5')
# select(path='z3')
# select(path='mathsat')
# select(path='z3(b)')
# select(path='yices2')
# select(path='aprove')

# classify('blan_sat', 'none', 'none')
# classify('z3_sat', 'none', 'none')
# classify('z3(b)_sat', 'none', 'none')
# classify('cvc5_sat', 'none', 'none')
# classify('aprove_sat', 'none', 'none')
# classify('yices2_sat', 'none', 'none')
# classify('mathsat_sat', 'none', 'none')

get_graph_sat()
# get_graph_sat('AProVE')
# get_graph_sat('calypto')
# get_graph_sat('Dartagnan')
# get_graph_sat('LassoRanker')
# get_graph_sat('leipzig')
# get_graph_sat('mcm')
# get_graph_sat('CInteger')
# get_graph_sat('ITS')
# get_graph_sat('SAT14')
# get_graph_sat('MathProblems')

# get_graph_sat(graph='new')
# get_graph_sat('AProVE')
# get_graph_sat('calypto')
# get_graph_sat('Dartagnan')
# get_graph_sat('LassoRanker')
# get_graph_sat('leipzig')
# get_graph_sat('mcm')
# get_graph_sat('CInteger')
# get_graph_sat('ITS')
# get_graph_sat('SAT14')
# get_graph_sat('MathProblems')