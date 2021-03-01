import numpy as np

# 一维数组
# a1 = np.array([1,2,3])
# print(a1)

# 二维数组
# a2 = np.array([[1,2,3],[4,5,6]])
# print(a2)

# 所有数据都是同一个数据类型
# a3 = np.array([[111,222,333],['aaa',444,555]])
# print(a3)

import matplotlib.pylab as plt

img_arr = plt.imread('hello.jpg')
# print(img_arr)
# print(len(img_arr))

plt.imshow(img_arr)
