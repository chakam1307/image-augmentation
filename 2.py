import shutil
import os
import random
import numpy as numpy
import cv2
import glob
from PIL import Image
from matplotlib import pyplot as plt


img = cv2.imread('./test/1.jpg', 0)
edges = cv2.Canny(img, 50, 100)

cv2.imwrite('./test/test.jpg', edges)

# edges.save('./test/test.jpg')
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()