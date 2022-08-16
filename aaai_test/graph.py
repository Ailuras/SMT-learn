from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

from get_data import get_data, get_data_new

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

def get_graph(category='none', type='log', graph='none'):
    
    # 生成数据
    if category == 'none':
        if graph == 'none':
            instances_ours, time_ours = get_data('./blan/', 'SAT_Split_100')
            instances_aprove, time_aprove = get_data('./aprove/', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data('./cvc5/', 'SAT_Split_100')
            instances_yices, time_yices = get_data('./yices2/', 'SAT_Split_100')
            instances_z3, time_z3 = get_data('./z3/', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data('./mathsat/', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data('./z3(b)/', 'SAT_Split_100')
        else:
            instances_ours, time_ours = get_data_new('./blan/', 'SAT_Split_100')
            instances_aprove, time_aprove = get_data_new('./aprove/', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data_new('./cvc5/', 'SAT_Split_100')
            instances_yices, time_yices = get_data_new('./yices2/', 'SAT_Split_100')
            instances_z3, time_z3 = get_data_new('./z3/', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data_new('./mathsat/', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data_new('./z3(b)/', 'SAT_Split_100')
    else:
        if graph == 'none':
            instances_ours, time_ours = get_data('./blan_classify/'+category+'.log', 'SAT_Split_100')
            instances_aprove, time_aprove = get_data('./aprove_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data('./cvc5_classify/'+category+'.log', 'SAT_Split_100')
            instances_yices, time_yices = get_data('./yices2_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3, time_z3 = get_data('./z3_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data('./mathsat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data('./z3(b)_classify/'+category+'.log', 'SAT_Split_100')
        else:
            instances_ours, time_ours = get_data_new('./blan_classify/'+category+'.log', 'SAT_Split_100')
            instances_aprove, time_aprove = get_data_new('./aprove_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5, time_cvc5 = get_data_new('./cvc5_classify/'+category+'.log', 'SAT_Split_100')
            instances_yices, time_yices = get_data_new('./yices2_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3, time_z3 = get_data_new('./z3_classify/'+category+'.log', 'SAT_Split_100')
            instances_cvc5b, time_cvc5b = get_data_new('./mathsat_classify/'+category+'.log', 'SAT_Split_100')
            instances_z3b, time_z3b = get_data_new('./z3(b)_classify/'+category+'.log', 'SAT_Split_100')
    

    # 生成图形
    plt.plot(instances_ours, time_ours, 'r', label='BLAN')
    plt.plot(instances_aprove, time_aprove, 'blue', label='APROVE')
    plt.plot(instances_cvc5, time_cvc5, 'green', label='CVC5')
    plt.plot(instances_cvc5b, time_cvc5b, 'orange', label='MATHSAT')
    plt.plot(instances_yices, time_yices, 'gold', label='YICES2')
    plt.plot(instances_z3, time_z3, 'violet', label='Z3')
    plt.plot(instances_z3b, time_z3b, 'lawngreen', label='Z3(B)')

    # 显示图形
    if graph == 'none':
        plt.ylabel('time (s)') # 横坐标轴的标题
        plt.xlabel('instances') # 纵坐标轴的标题
    else:
        plt.ylabel('numbers') # 横坐标轴的标题
        plt.xlabel('time (s)') # 纵坐标轴的标题
    plt.legend() # 显示图例, 图例中内容由 label 定义
    if type == 'log':
        plt.yscale("log")
    # ax = plt.gca()
    # # y 轴用科学记数法
    # ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
    if category == 'none':
        if type == 'log':
            plt.savefig('result/experiments_log.pdf')
        else:
            plt.savefig('result/experiments.pdf')
    else:
        if type == 'log':
            plt.savefig('result/experiments_' + category + '_log.pdf')
        else:
            plt.savefig('result/experiments_' + category + '.pdf')
    # plt.close()
    plt.show()
    

# get_graph()
# get_graph('AProVE')
# get_graph('calypto')
# get_graph('Dartagnan')
# get_graph('LassoRanker')
# get_graph('leipzig')
# get_graph('mcm')
# get_graph('CInteger')
# get_graph('ITS')
# get_graph('SAT14')
# get_graph('MathProblems')

get_graph(type='none')
# get_graph('AProVE', type='none')
# get_graph('calypto', type='none')
# get_graph('Dartagnan', type='none')
# get_graph('LassoRanker', type='none')
# get_graph('leipzig', type='none')
# get_graph('mcm', type='none')
# get_graph('CInteger', type='none')
# get_graph('ITS', type='none')
# get_graph('SAT14', type='none')
# get_graph('MathProblems', type='none')

get_graph(type='none', graph='new')
# get_graph('AProVE', type='none', graph='new')
# get_graph('calypto', type='none', graph='new')
# get_graph('Dartagnan', type='none', graph='new')
# get_graph('LassoRanker', type='none', graph='new')
# get_graph('leipzig', type='none', graph='new')
# get_graph('mcm', type='none', graph='new')
# get_graph('CInteger', type='none', graph='new')
# get_graph('ITS', type='none', graph='new')
# get_graph('SAT14', type='none', graph='new')
# get_graph('MathProblems', type='none', graph='new')