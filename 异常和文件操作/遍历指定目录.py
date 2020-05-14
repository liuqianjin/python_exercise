import os
path = 'C:\\demo'
print('【',path,'】目录八廓的文件和目录')
for root , dirs, files in os.walk(path,topdown=True):
    for name in dirs:
        print('#',os.path.join(root,name))
    for name in files:
        print('*',os.path.join(root,name))