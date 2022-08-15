# 对文件进行分类
python classify.py none none
# 获取运行时间大于10s的文件
# python classify.py 10 none
# 获取运行时间小于120s的文件
# python classify.py none 120

# 绘制散点图
# 在这边改后缀
suffix=_classify
python compare.py hhh$suffix "z3(b)"$suffix
python compare.py hhh$suffix z3$suffix
python compare.py hhh$suffix cvc5$suffix
python compare.py hhh$suffix yices2$suffix
python compare.py hhh$suffix aprove$suffix
python compare.py hhh$suffix mathsat$suffix

# 绘制曲线图，想修改对应文件夹，需要改python文件
python graph.py
python graph_sat.py

# 删除多余文件夹
./del.sh

# 获取hhh能解其他都不能解的例子
# python select_timeout.py