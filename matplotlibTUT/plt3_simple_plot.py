# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 3 - simple plot
"""
Please note, this script is for python3+.
If you are using python2+, please modify it accordingly.
"""

import matplotlib.pyplot as plt
import numpy as np

# 定义x&y变量
x = np.linspace(-1, 1, 50)
y_1 = 2*x + 1
y_2 = x**2

# .plot: 画x&y的图
plt.plot(x, y_2)
# .show才会画出来
plt.show()
