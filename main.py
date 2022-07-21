import shutil
import os
import random
import numpy as numpy
import cv2
import glob
from PIL import Image

required_img = 20

for (path, dir, files) in os.walk("./data/"):
    if len(files) == 0:
        continue
    cate = path[-13:]
    num_aug = required_img - len(files)
    n = 100

    for i in range(num_aug):
        idx = random.randrange(0, len(files))
        img = files[idx]
        img_path = "{}/{}".format(path, img)
        
        image = Image.open(img_path)
        random_augment = random.randrange(1,4)
        
        if random_augment == 1:
            invert = image.transpose(Image.FLIP_LEFT_RIGHT)
            invert.save(path + '/' + str(n) + '.jpg')
            n += 1
        elif random_augment == 2:
            rotate = image.rotate(random.randrange(-20, 20))
            rotate.save(path + '/' +str(n) + '.jpg')
            n += 1
        elif random_augment == 3:
            invert = image.transpose(Image.FLIP_LEFT_RIGHT)
            invert_rotate = invert.rotate(random.randrange(-20, 20))
            invert_rotate.save(path + '/' +str(n) + '.jpg')
            n += 1
