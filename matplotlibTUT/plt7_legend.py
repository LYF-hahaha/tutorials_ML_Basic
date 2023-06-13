# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 7 - legend
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

# 多数据区分（有一个说明框框，说明每条线代表什么意思）

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 最简单的画图指令
plt.plot(x, y1, label='linear line')
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
# 并输出图例说明
plt.legend(loc='upper right')

# plt是有返回值的，可以赋值给l1
# 如果想把返回值传入legend的handle中，后面需要加个逗号","
# the "," is very important in here l1, = plt... and l2, = plt... for this step
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

# handel: 给与一个所要放如图中的线
# loc=best: 自己找一个没那么多数据的地方放着（你拖动图片的时候会自动调节）
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
# 若只想打一个数据的说明，可做如下操作
# plt.legend(handles=[l1,], labels=['aaa',],  loc='best')


"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    The *loc* location codes are::

          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

plt.show()
