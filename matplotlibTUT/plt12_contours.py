# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 12 - contours
# 等高线
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    # the height function
    # 一个三维空间曲面函数
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

# x y的范围
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 定义底图为网格
# 因为等高线就是在基础网格上fill高度
X,Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
# 曲面加颜色：contour+f(f=fill)
plt.contourf(X, Y, f(X, Y), # x y z
             10, # 将高度分为多少段来画图（如果是0，就是一条线，分为2段）
             alpha=.75,
             cmap=plt.cm.cool) # z的值=热力图(hot cool)

# use plt.contour to add contour lines
# 等高线的线
C = plt.contour(X, Y, f(X, Y), 10, colors='black', linewidth=.5)
# adding label
plt.clabel(C, # 线
           inline=True, # 线是否穿过文字
           fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()

