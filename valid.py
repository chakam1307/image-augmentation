import os
import shutil

for (path, dir, files) in os.walk("./data/"):
    num = -1
    cate = path[-13:]
    for filename in files:
        ext = os.path.splitext(filename)

        ext = int(ext[0])
        src = path+'/'+filename
        if num < 7:
            num += 1
        des_path = './DT/'+ cate + '_' + str(num)
        
        if not os.path.exists(des_path):
            os.mkdir(des_path)
        shutil.move(src, des_path)

        
