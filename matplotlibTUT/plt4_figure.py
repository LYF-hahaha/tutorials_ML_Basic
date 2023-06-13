# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 4 - figure
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

# fig表示窗口
# 有时会需要多个窗口同时显示不同图片
# 一个figure下面对应一个窗口中的图片内容
# 新出一个fig代表一个新窗口
plt.figure()
plt.plot(x, y1)

# num表示这个窗口的标题内容；figsize表示窗口尺寸（但显示出来后也可以用鼠标拖动）
plt.figure(num=3, figsize=(8, 10),)
plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
# 可以在一个fig中画多个曲线
# 可以设定颜色、线宽、线型等参数
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 全画出来
plt.show()
