import shutil
from os import walk
import sys

def joinfiles(BasePath,filename):
    with open(filename,'wb') as wfd:
        for f in next(walk(BasePath), (None, None, []))[2]:
            with open(BasePath + f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)

joinfiles(f"./files/{sys.argv[1]}/",f"./files/{sys.argv[2]}")