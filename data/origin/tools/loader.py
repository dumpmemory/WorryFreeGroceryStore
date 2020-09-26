#encoding utf8
# author : yang
# date : 20191124
from .common_tools import timer
import pickle
# 功能：存储 pkl 数据
@timer
def saveDict(obj,outputPath,name):
    if "." not in name:
        fileName = f"{outputPath}{name}.pkl"
    else:
        fileName = f"{outputPath}{name}"
    with open(fileName, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# 功能：加载 pkl 数据
@timer
def loadDict(outputPath,name):
    if "." not in name:
        fileName = f"{outputPath}{name}.pkl"
    else:
        fileName = f"{outputPath}{name}"
    with open(fileName, 'rb') as f:
        return pickle.load(f)

# 功能：字典数据分割
@timer
def dictCutBatchSave(inputPath,outputPath,fileName,batchSize):
    '''
        功能：字典数据分割，将数据分割成多个小块，便于保存
        Args: 
            inputPath     String
            outputPath    String 
            fileName      String
            batchSize     int        分割粒度
    '''
    dictData = loadDict(inputPath,fileName)
    dictLen = len(dictData)
    for i in range(0, dictLen, batchSize):
        saveDict(dict(list(dictData.items())[i:i+batchSize]),outputPath,f"{fileName}_{i}")

# 功能：加载指定目录下指定字典文件 并合并 成一个字典  
@timer
def dictLoadMerge(inputPath,keyName):
    '''
        功能：加载指定目录下指定字典文件 并合并 成一个字典 
        Args:
            inputPath     String     输入路径 
            keyName       String     包含 keyName 的文件才加载
        Return:
            mainDict      Dict       合并后的字典
    '''
    import os
    fileNameList = os.listdir(inputPath)
    mainDict = {}
    for fileName in fileNameList:
        if keyName in fileName:
            mainDict.update(loadDict(inputPath,fileName))
    return mainDict


