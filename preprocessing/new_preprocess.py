import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image , ImageOps

count = 0
dst_dir = r"D:\build my dl NN test\imagegen"
base_dir = r"D:\build my dl NN test\imagegen"
path_test_image = os.path.join(base_dir+"\\"+"20180506101026.jpg")
image_color = cv2.imread(path_test_image)

new_shape = (image_color.shape[1]*2 , image_color.shape[0]*2)
image_color = cv2.resize(image_color, new_shape)
image = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)


cv2.threshold(image, 90, 255, 1, image)
image = cv2.blur(image, (4, 4))
cv2.imshow("asdf",image)
cv2.waitKey()
cv2.imwrite('1.jpg', image)

image_file = Image.open("1.jpg")

inverted_image = ImageOps.invert(image_file)
inverted_image.save('1.jpg')
inverted_image.show()

# horizontal_sum = np.sum(adaptive_threshold, axis=1)
#
# plt.plot(horizontal_sum, range(horizontal_sum.shape[0]))
# plt.gca().invert_yaxis()
# plt.show()
