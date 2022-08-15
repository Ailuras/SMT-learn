from cProfile import label
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import sys

from get_compare import get_data

def get_compare(a, b, category='none', type='log'):
    # 生成数据
    if category == 'none':
        times, times2= get_data('./'+a+'/', './'+b+'/', 'SAT_Split_100')
    else:
        times, times2= get_data('./'+a+'/'+category+'.log', './'+b+'/'+category+'.log', 'SAT_Split_100')

    # 生成图形
    plt.figure(figsize=(8, 8))
    
    plt.scatter(times[0], times[1], s=1, c='purple', marker="x", linewidth=5, alpha=0.25)
    plt.scatter(times2[0], times2[1], s=1, c='peru', marker="x", linewidth=5, alpha=0.25)
    x = [i for i in range(1500)]
    plt.plot(x, x, c='black', linewidth=0.5)

    # 显示图形
    plt.xlabel(a.upper() + ' (s)') # 横坐标轴的标题
    plt.ylabel(b.upper() + ' (s)') # 纵坐标轴的标题

    plt.xlim(0, 1300)
    plt.ylim(0, 1300)
    
    # ax = plt.gca()
    # ax.set_xticks = [10, 20, 30]
    # ax.set_yticks = [10, 20, 30]
    if type == 'log':
        plt.xscale('symlog')
        plt.yscale('symlog')
    # plt.xticks([0, 50, 100, 200, 400, 600, 800, 1000, 1200, 1300], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], fontproperties='STKAITI')
    
    # plt.yscale("log")
    # plt.xscale("log")
    if category == 'none':
        if type == 'log':
            plt.savefig('./result/'+a.upper() + '_VS_' + b.upper() + '(log)' +'.pdf')
        else:
            plt.savefig('./result/'+a.upper() + '_VS_' + b.upper() +'.pdf')
    else:
        if type == 'log':
            plt.savefig('./result/'+a.upper() + '_VS_' + b.upper() + '_' + category + '(log)' +'.pdf')
        else:
            plt.savefig('./result/'+a.upper() + '_VS_' + b.upper() + '_' + category +'.pdf')
    # plt.show()
    plt.close()
    
a = sys.argv[1]
b = sys.argv[2]

get_compare(a, b)
get_compare(a, b, 'AProVE')
get_compare(a, b, 'calypto')
get_compare(a, b, 'Dartagnan')
get_compare(a, b, 'LassoRanker')
get_compare(a, b, 'leipzig')
get_compare(a, b, 'mcm')
get_compare(a, b, 'CInteger')
get_compare(a, b, 'ITS')
get_compare(a, b, 'SAT14')
get_compare(a, b, 'MathProblems')

get_compare(a, b, type='none')
get_compare(a, b, 'AProVE', type='none')
get_compare(a, b, 'calypto', type='none')
get_compare(a, b, 'Dartagnan', type='none')
get_compare(a, b, 'LassoRanker', type='none')
get_compare(a, b, 'leipzig', type='none')
get_compare(a, b, 'mcm', type='none')
get_compare(a, b, 'CInteger', type='none')
get_compare(a, b, 'ITS', type='none')
get_compare(a, b, 'SAT14', type='none')
get_compare(a, b, 'MathProblems', type='none')