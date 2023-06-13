# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 6 - axis setting
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new ticks
new_ticks_x = np.linspace(-1, 2, 5)
plt.xticks(new_ticks_x)
# set tick labels
# plt.yticks([-2, -1.8, -1, 1.22, 3],
#            ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
new_ticks_y = np.linspace(-2, 2, 5)
plt.yticks(new_ticks_y)
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

# gca = 'get current axis'
# 获取当前坐标轴
ax = plt.gca()
# 获取轴的“脊椎”（也就是图片的四个边框）
ax.spines['right'].set_color('none') # 把右边的轴设置成透明
ax.spines['top'].set_color('none') # 同上

# 指定x轴
ax.xaxis.set_ticks_position('bottom')
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]

# 另一个轴(y)的哪个位置与bottom轴相交
# 即y轴的哪个位置会与x轴相交
ax.spines['bottom'].set_position(('data', 1))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis (0.1=10%)
# data: depend on y data （y轴的1与x轴相交）
# outward: y轴的最底端立在x轴上

# 指定y轴
ax.yaxis.set_ticks_position('left')
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

# 另一个轴(x)的哪个位置与left轴相交
# 即在x轴上的哪个位置会与y轴相交
ax.spines['left'].set_position(('data', 0.1))
plt.show()
