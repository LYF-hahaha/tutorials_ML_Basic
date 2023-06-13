# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 19 - animation
# 动画
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.

Tutorial reference:
http://matplotlib.org/examples/animation/simple_anim.html

More animation example code:
http://matplotlib.org/examples/animation/
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

# 到此为止，还只是一个静态图
x = np.arange(0, 2*np.pi, 0.01)
# 画出这么一根线来
# 因为返回值是个列表
line, = ax.plot(x, np.sin(x))

# y = np.sin(x)
# plt.plot(x, y)
# plt.show()


def animate(i):
    # line的y数据更新成新的数据 np.sin(x + i/10.0)
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    # y的初始值
    line.set_ydata(np.sin(x))
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
ani = animation.FuncAnimation(fig=fig, # 需要传进去的图框
                              func=animate, # 动画函数
                              frames=100, # 动画总帧数(100个时间点)
                              init_func=init, # 动画初始的样子
                              interval=20, # 更新帧的频率
                              blit=False) # 是否更新整张图片，还是只更新变化了的地方

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
