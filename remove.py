import os

for (path, dir, files) in os.walk("./data/"):
    for filename in files:
        ext = os.path.splitext(filename)
        ext = int(ext[0])
        if ext >= 100 and ext < 130:
            os.remove(path+'/'+filename)