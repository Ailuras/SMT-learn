from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

from get_data import get_data

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


# 生成数据
instances_aprove, time_aprove = get_data('./1200_aprove/', 'SAT_Split_100')
instances_cvc5, time_cvc5 = get_data('./1200_cvc5/', 'SAT_Split_100')
instances_ours, time_ours = get_data('./1200_ours/', 'SAT_Split_100')
instances_yices, time_yices = get_data('./1200_yices2/', 'SAT_Split_100')
instances_z3, time_z3 = get_data('./1200_z3/', 'SAT_Split_100')
instances_cvc5b, time_cvc5b = get_data('./1200_cvc5(b)/', 'SAT_Split_100')
instances_z3b, time_z3b = get_data('./1200_z3(b)/', 'SAT_Split_100')

# 生成图形
plt.plot(instances_aprove, time_aprove, label='APROVE')
plt.plot(instances_cvc5, time_cvc5, label='CVC5')
plt.plot(instances_cvc5b, time_cvc5b, label='CVC5(B)')
plt.plot(instances_yices, time_yices, label='YICES2')
plt.plot(instances_z3, time_z3, 'blue', label='Z3')
plt.plot(instances_z3b, time_z3b, label='Z3(B)')
plt.plot(instances_ours, time_ours, 'r', label='OURS')


# 显示图形
plt.ylabel('time (s)') # 横坐标轴的标题
plt.xlabel('instances') # 纵坐标轴的标题
plt.legend() # 显示图例, 图例中内容由 label 定义
ax = plt.gca()
# y 轴用科学记数法
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
plt.savefig('experiments.pdf')
plt.show()

