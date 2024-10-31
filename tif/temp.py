from pathlib import Path

import cv2
from skimage import io
file = Path("./1.tif")
try:
    _ = io.imread(file, as_gray=False)
    im_rgb = cv2.cvtColor(_, cv2.COLOR_BGR2RGB)
    cv2.imshow("image", im_rgb)
    cv2.waitKey(0) #等待按键
except Exception as e:
    # 说明文件损坏了
    print(file)