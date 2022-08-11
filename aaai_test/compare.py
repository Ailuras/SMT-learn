from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import sys

from get_compare import get_data

a = sys.argv[1]
b = sys.argv[2]

# 生成数据
times= get_data('./1200_'+a.lower()+'/', './1200_'+b.lower()+'/', 'SAT_Split_100')

# 生成图形
plt.scatter(times[0], times[1], s=1, c='black')
x = [i for i in range(1200)]
plt.plot(x, x)

# 显示图形
plt.xlabel(a.upper() + ' (s)') # 横坐标轴的标题
plt.ylabel(b.upper() + ' (s)') # 纵坐标轴的标题
plt.savefig(a.upper() + '_' + b.upper() +'.pdf')
plt.show()

