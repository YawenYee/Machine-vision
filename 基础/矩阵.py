import numpy as np
# 合并矩阵
a = np.arange(16).reshape(4, 4)
b = np.floor(5*np.random.random((2, 4)))
c = np.ceil(6*np.random.random((4, 2)))
d = np.vstack([a, b])  # 纵向合并矩阵
e = np.hstack([a, c])  # 左右合并矩阵
print(d)
print(e)

