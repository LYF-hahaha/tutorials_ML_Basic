# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 18 - secondary y axis
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.python-course.eu/matplotlib_multiple_figures.php
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 *y1
y3 = 0.02* x**3

# 定义子图1&坐标轴
fig, ax1 = plt.subplots()
# 让2个子图的x轴一样，同时创建副坐标轴(y)
# 若是twiny，则是让两个子图的y轴一样，同时创建副x轴
# 而画出来的副坐标轴之所以恰好与主坐标反着，是因为y2恰好是y1的负的(若改成y3，就完全不一样了)
# 可以理解为自fit的过程
ax2 = ax1.twinx()    # mirror the ax1

# 画图
l1, = ax1.plot(x, y1, 'g-')
l2, = ax2.plot(x, y3, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
# 次坐标轴
ax2.set_ylabel('Y3 data', color='b')

# plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['y1', 'y3'],  loc='best')


plt.show()
