from pprint import pprint

import cv2
import scipy.io
import numpy as np

# 读取MAT文件
data = scipy.io.loadmat('control_30R.mat')
print(data.keys())
print(data["__header__"])
print(data["__version__"])
print(data["__globals__"])

print(type(data["sBW"]))
print(data["sBW"].shape)
sBW = data["sBW"][0,0] # type: numpy.void
BW = sBW["BW"]
print(np.unique(BW))
BW[BW == 1] = 255
cv2.imwrite("demo.jpg", BW)