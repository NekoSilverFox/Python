# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 0:33
# @Author  : NekoSilverfox
# @FileName: main.py
# @Software: PyCharm
# @Versions: v0.1
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


# 创建一个等差数列，从0开始到100，由1000个数构成
x = np.linspace(0, 100, 1000)

y = np.sin(x)

"""plt.plot
    - x: x 轴上的数据
    - y: y 轴上的数据
    - c: 线条颜色
    - lw: 线条宽度
    - ls: 线条风格
        `-` 实线
        `--` 虚线
        `-.` 点划线
        `.` 实点线
"""
plt.plot(x, y, c='red', lw=2, ls='-')
plt.show()

