from typing import List
import matplotlib.pyplot as plt  # 导入包

fig = plt.figure()  # 创建空图
plt.figure(dpi=100)
x_label = []  # x轴的坐标
for i in range(20):
    x_label.insert(i, 100+i*100)

y1 = [0.00287,
0.02544,
0.07147,
0.12149,
0.23264,
0.52400 ,
0.80274,
1.12345,
1.52641,
3.08614,
3.99593,
4.33147,
6.64065,
6.62336,
11.66413,
20.70261,
29.09317,
41.05284,
54.47069,
59.06919

      ]  # y轴坐标

y2 = [0.02012,
0.02043,
0.01628,
0.04315,
0.07015,
0.10612,
0.17987,
0.28216,
0.61573,
0.65739,
0.81765 ,
1.40075,
0.99866,
1.08468,
1.38936,
2.29651,
2.14740 ,
2.86001,
3.08149,
4.24567,

      ]

# y3 = [0.10777,
# 0.12599,
# 0.25242,
# 0.32449,
# 0.59480,
# 0.61342,
# 0.88443,
# 1.30487,
# 1.45609,
# 2.00889,
# 2.31689,
# 3.76254,
# 3.94145,
# 4.40344,
# 4.71807,
# 5.62649,
# 6.35896,
# 9.09975,
# 8.64596,
# 9.94972
#       ]


p1,=plt.plot(x_label, y1, color='r', linewidth=1.0,
         linestyle='-')  # 构建折线图，可以设置线宽，颜色属性
p2,=plt.plot(x_label, y2, color='g', linewidth=1.0,
         linestyle='-')  # 构建折线图，可以设置线宽，颜色属性
# p3,=plt.plot(x_label, y3, color='m', linewidth=1.0,
#          linestyle='-')  # 构建折线图，可以设置线宽，颜色属性

plt.legend([p1,p2],["original mnk sorting","4x4-blocks"],loc='best')

plt.title("The run-time of mnk sorting and 4x4-blocks")  # 设置标题，这里只能显示英文，中文显示乱码

plt.ylabel("Run-time(s)")  # 设置y轴名称

plt.xlabel("The number of rows and columns")  # 设置x轴名称

plt.show()  # 将图形显示出来
