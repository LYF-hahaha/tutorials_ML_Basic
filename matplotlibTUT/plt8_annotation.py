# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 8 - annotation
# 图片中添加注解
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.

Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html

Mathematical expressions:
http://matplotlib.org/users/mathtext.html#mathtext-tutorial
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y, color = 'red')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 画指出数据的虚线和高亮数据的点
# 需要标注的相关点
x0 = 1
y0 = 2*x0 + 1
# 画出连接(x0,x0)和(0,y0)两个点的线
# k：black
# --: 虚线
plt.plot([x0, x0, ], [0, y0, ], 'k--', linewidth=2.5)
# 画出一系列点（指定）
plt.scatter([x0, ], [y0, ], s=50, color='b')

# method 1:
#####################
#
plt.annotate(r'$2x+1=%s$' % y0, # 输出的文字内容（label）
             xy=(x0, y0), # 给定label的起始坐标
             xycoords='data', # 以某一个值为起始坐标（跟上面的参数一起用）
             xytext=(+30, -30), # 标签的文字描述起始点（相对于xy的偏置值）
             textcoords='offset points', # 偏置模式（跟上面的参数一起用的）
             fontsize=16,
             # 指向数据的方向线
             arrowprops=dict(arrowstyle='->', # 箭头类型
                             connectionstyle="arc3,rad=.2")) # 箭头是否有弧度以及相应的半径

# method 2:
########################
# 直接在fig里输出文字
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()
