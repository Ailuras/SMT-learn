from cProfile import label
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import sys

from get_compare import get_data

a = sys.argv[1]
b = sys.argv[2]

# 生成数据
times, times2= get_data('./'+a.lower()+'/', './'+b.lower()+'/', 'SAT_Split_100')

# 生成图形
plt.scatter(times[0], times[1], s=1, c='purple', marker="x", linewidth=5, alpha=0.4)
plt.scatter(times2[0], times2[1], s=1, c='peru', linewidth=5, alpha=0.4)
x = [i for i in range(1500)]
plt.plot(x, x, c='red', linewidth=0.5)

# 显示图形
plt.xlabel(a.upper() + ' (s)') # 横坐标轴的标题
plt.ylabel(b.upper() + ' (s)') # 纵坐标轴的标题

# plt.xlim(0, 1300)
# plt.ylim(0, 1300)
plt.yscale("log")
plt.xscale("log")

plt.savefig(a.upper() + '_' + b.upper() +'.pdf')
plt.show()

