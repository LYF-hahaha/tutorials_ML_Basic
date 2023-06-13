# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 16 - grid
# 把子图分成小格子
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
Tutorial reference:
http://matplotlib.org/users/gridspec.html
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1: subplot2grid
##########################
plt.figure()
# 子图1的占位说明
ax1 = plt.subplot2grid((3, 3), # 3x3的格子
                       (0, 0), # 起始处为0,0
                       colspan=3)  # 图片跨3列
# stands for axes
# 子图1画线
ax1.plot([1, 2], [2, 1])
# 子图1的title
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.scatter([1,3], [3,1])
ax2.set_title('ax2_title')

ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
# ax设置label
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

ax5 = plt.subplot2grid((3, 3), (2, 1))

# method 2: gridspec
#########################
plt.figure()
# 先定义网格尺寸
gs = gridspec.GridSpec(3, 3)
# use index from 0
# 说明子图占位
ax6 = plt.subplot(gs[0, :]) # 第0行全部
ax7 = plt.subplot(gs[1, :2]) # 第1行 至第3列
ax8 = plt.subplot(gs[1:, 2]) # 第1~2行 第3列
ax9 = plt.subplot(gs[-1, 0]) # 第3行 第0列
ax10 = plt.subplot(gs[-1, -2]) # 第3行 第2列

# method 3: easy to define structure
####################################
# fig=f
# 提前告知格式
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, # 网格尺寸
                                               sharex=True, sharey=True) # 是否共享坐标轴
# 只有11有图
ax11.scatter([1, 1], [0.5, 1.6])

plt.tight_layout()
plt.show()
