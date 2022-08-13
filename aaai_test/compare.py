from cProfile import label
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import sys

from get_compare import get_data

def get_compare(a, b, category):
    # 生成数据
    times, times2= get_data('./'+a+'_classify/'+category+'.log', './'+b+'_classify/'+category+'.log', 'SAT_Split_100')

    # 生成图形
    plt.scatter(times[0], times[1], s=1, c='purple', marker="x", linewidth=5, alpha=0.25)
    plt.scatter(times2[0], times2[1], s=1, c='peru', linewidth=5, alpha=0.25)
    x = [i for i in range(1500)]
    plt.plot(x, x, c='red', linewidth=0.5)

    # 显示图形
    plt.xlabel(a.upper() + ' (s)') # 横坐标轴的标题
    plt.ylabel(b.upper() + ' (s)') # 纵坐标轴的标题

    plt.xlim(0, 1300)
    plt.ylim(0, 1300)
    # plt.yscale("log")
    # plt.xscale("log")

    plt.savefig('./result/'+a.upper() + '_' + b.upper() + '_' + category +'.pdf')
    # plt.show()
    
a = sys.argv[1]
b = sys.argv[2]

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