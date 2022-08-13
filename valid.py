import os
import shutil

data_path = './B7340_헤어드라이기/'


for (path, dir, files) in os.walk(data_path):
    num = -1
    cate = path[-13:]
    for filename in files:
        ext = os.path.splitext(filename)

        ext = int(ext[0])
        src = path+'/'+filename
        if num < 7:
            num += 1
        des_path = './DT' + data_path[1:]+ cate + '_' + str(num)
        
        if not os.path.exists(des_path):
            os.mkdir(des_path)
        shutil.move(src, des_path)

        
