import shutil
import os
import cv2
import glob
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance, ImageChops
import numpy as np
import random

required_img = 20
aug_path = "DATA DIR"

for (path, dir, files) in os.walk(aug_path):
    if len(files) == 0:
        continue
    num_aug = required_img - len(files)
    n = 100

    for i in range(num_aug):
        idx = random.randrange(0, len(files))
        img = files[idx]
        img_path = "{}/{}".format(path, img)
        
        image = Image.open(img_path)
        image = image.convert('L')
        image = image.resize((300, 300))
        random_augment = random.randrange(1,6)
        
        # 좌우 이동
        if random_augment == 1:
            width, height = image.size
            shift = random.randint(0, width * 0.2)
            horizonal_shift_image = ImageChops.offset(image, shift, 0)
            horizonal_shift_image.paste((0), (0, 0, shift, height))
            horizonal_shift_image.save(path + '/' + str(n) + '.jpg')
            n += 1

        # 상하 이동
        elif random_augment == 2:
            width, height = image.size
            shift = random.randint(0, height * 0.2)
            vertical_shift_image = ImageChops.offset(image, 0, shift)
            vertical_shift_image.paste((0), (0, 0, width, shift))
            vertical_shift_image.save(path + '/' +str(n) + '.jpg')
            n += 1

        # 회전
        elif random_augment == 3:
            rotate_image = image.rotate(random.randint(-30, 30))
            rotate_image.save(path + '/' +str(n) + '.jpg')
            n += 1

        # 기울기
        elif random_augment == 4:
            cx, cy = 0, random.uniform(0.0, 0.3)
            shear_image = image.transform(
                image.size,
                method=Image.AFFINE,
                data=[1, cx, 0,
                    cy, 1, 0,])
            shear_image.save(path + '/' +str(n) + '.jpg')
            n += 1

        # 확대 축소
        elif random_augment == 5:
            zoom = random.uniform(0.7, 1.3) #0.7 ~ 1.3
            width, height = image.size
            x = width / 2
            y = height / 2
            crop_image = image.crop((x - (width / 2 / zoom), y - (height / 2 / zoom), x + (width / 2 / zoom), y + (height / 2 / zoom)))
            zoom_image = crop_image.resize((width, height), Image.LANCZOS)
            zoom_image.save(path + '/' +str(n) + '.jpg')
            n += 1
            
