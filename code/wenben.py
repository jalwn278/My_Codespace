import os.path
def getTxtPaths(dirpath):
    paths = []
    filenames = os.listdir(dirpath)
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            paths.append(filepath)
    return paths
for path in getTxtPaths('学生反馈'):
    print(path)

#读取一个txt文件
def readOneTxt(filepath):
    try:
        file=open(filepath,'r')
        text=file.read()
        file.close()
        return text
    except:
        return ''
print(readOneTxt('test.txt'))

#文件合并
def mergeTxts(srcPaths,destPath):
    destFile = open(destPath,'w')
    for srcPath in srcPaths:
        test=readOneTxt(srcPath)
        if test!='':
            destFile.write(test)
            destFile.write('\n'*2+'-'*50+'\n'*2)
    destFile.close()
    return os.path.realpath(destPath)
srcPaths=getTxtPaths('红楼梦')
mergeTxts(srcPaths,'result.txt')
print(readOneTxt('result.txt'))