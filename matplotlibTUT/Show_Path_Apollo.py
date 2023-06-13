import os
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import animation


def load_path(path, filename):
    data = os.path.join(path, filename)
    with open(data) as f:
        traj = f.read().split('\n')
    x = []
    y = []
    print("loading position...")
    with tqdm(total=len(traj)-1) as t:
        for i in range(len(traj)-1):
            a = traj[i].split()
            x_pos = float(a[2])
            y_pos = float(a[3])
            x.append(x_pos)
            y.append(y_pos)
            t.update(1)
        t.close()
    f.close()
    return x, y


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def layout_plot(x, y):

    x_nom = normalization(x)
    y_nom = normalization(y)
    T = np.arctan2(x_nom, y_nom)  # for color later on
    # x_s x_1 x_2 x_3 x_e
    x_label = [x[0], x[int(len(x)/4)], x[int(len(x)/2)], x[int(3*len(x)/4)], x[-1]]
    y_label = [y[0], y[int(len(x)/4)], y[int(len(x)/2)], y[int(3*len(x)/4)], y[-1]]
    # alpha 透明度
    plt.scatter(x, y, s=25, c=T, alpha=.7)

    plt.annotate(r'$Start Point$',  # 输出的文字内容（label）
                 xy=(x_label[0], y_label[0]),  # 给定label的起始坐标
                 xycoords='data',  # 以某一个值为起始坐标（跟上面的参数一起用）
                 xytext=(+30, -30),  # 标签的文字描述起始点（相对于xy的偏置值）
                 textcoords='offset points',  # 偏置模式（跟上面的参数一起用的）
                 fontsize=12,
                 # 指向数据的方向线
                 arrowprops=dict(arrowstyle='->',  # 箭头类型
                                 connectionstyle="arc3,rad=.2"))  # 箭头是否有弧度以及相应的半径
    plt.annotate(r'$25\%$', xy=(x_label[1], y_label[1]), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->',  connectionstyle="arc3,rad=.2"))
    plt.annotate(r'$50\%$', xy=(x_label[2], y_label[2]), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->',  connectionstyle="arc3,rad=.2"))
    plt.annotate(r'$75\%$', xy=(x_label[3], y_label[3]), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->',  connectionstyle="arc3,rad=.2"))
    plt.annotate(r'$End Point$', xy=(x_label[4], y_label[4]), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->',  connectionstyle="arc3,rad=.2"))
    plt.show()


def tj_anim(x, y):
    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    line, = plt.plot([], [], animated=True)

    pos_x = x
    pos_y = y
    x_a = []
    y_a = []

    # Init only required for blitting to give a clean slate.
    def init():
        ax.set_xlim(min(pos_x), max(pos_x))
        ax.set_ylim(min(pos_y), max(pos_y))
        return line,

    def animate(i):
        # line的y数据更新成新的数据 np.sin(x + i/10.0)
        x_a.append(pos_x[i])
        y_a.append(pos_y[i])
        line.set_data(x_a, y_a)  # update the data
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    # blit=True dose not work on Mac, set blit=False
    # interval= update frequency
    ani = animation.FuncAnimation(fig=fig,  # 需要传进去的图框
                                  func=animate,  # 动画函数
                                  frames=len(x),  # 动画总帧数(100个时间点)
                                  init_func=init,  # 动画初始的样子
                                  interval=0.5,  # 更新帧的频率
                                  blit=True)  # 是否更新整张图片，还是只更新变化了的地方

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    ani.save(filename='./trajectory.gif', fps=1650, writer="pillow")
    plt.show()


if __name__ == '__main__':
    path = './'
    file_name = 'gt_poses.txt'
    loc_x, loc_y = load_path(path, file_name)
    loc_x = np.array(loc_x)
    loc_y = np.array(loc_y)

    # layout_plot(loc_x, loc_y)
    tj_anim(loc_x, loc_y)
