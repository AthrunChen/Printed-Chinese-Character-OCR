import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image , ImageOps



count = 0
dst_dir = r"D:\build my dl NN test\imagegen"
base_dir = r"D:\build my dl NN test\imagedataset"
path_test_image = os.path.join(base_dir+"\\"+"IMG_20180506_193859.jpg")
image_color = cv2.imread(path_test_image)
scale = 1

if image_color.shape[0] >1600 :
    scale = int(image_color.shape[0]/1000)
print(scale)
new_shape = (int(image_color.shape[1] / scale), int(image_color.shape[0] / scale))
image_color = cv2.resize(image_color, new_shape)
image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

true_width = int(1.63 * image.shape[0])
width_cut_start = int((image.shape[1]-true_width)/2)
width_cut_end = int((image.shape[1]+true_width)/2)
image = image[:, width_cut_start:width_cut_end]

cv2.threshold(image, 90, 255, 1, image)

temp1 = int(image.shape[1]/2)
temp2 = int(image.shape[0]/2)
image[:temp2, temp1:] = 0
cv2.imwrite("processed.jpg",image)
# cv2.imshow('binary image', image2)
# print(image2.shape)
# cv2.waitKey()


cv2.imshow('binary image',image)
print(image.shape)
cv2.waitKey()
horizontal_sum = np.sum(image, axis=1)
print(horizontal_sum.shape)
print(horizontal_sum)
plt.plot(horizontal_sum, range(horizontal_sum.shape[0]))
plt.gca().invert_yaxis()
# plt.show()