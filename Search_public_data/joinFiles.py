import shutil
from os import walk

def joinfiles(BasePath,filename):
    with open(filename,'wb') as wfd:
        for f in next(walk(BasePath), (None, None, []))[2]:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
                
print(next(walk("./files/EMPRESAS/"), (None, None, []))[2])