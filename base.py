#encoding utf8
# author : yang
# date : 20191124
from tools.loader import loadDict

dictPath = "data/dict/"
dictName = "constellation"

constellationDict = loadDict(dictPath,dictName)
print(f"constellationDict:{constellationDict}")
# constellation = "白羊座"
# mess = "来自遥远的星星你，是否也会怀念回家的路？"
# if constellation in constellationDict:
#     mess = f"{constellation}的运势：时间：{constellationDict[constellation]['startTime']}-{constellationDict[constellation]['endTime']}，特点：{constellationDict[constellation]['特点']}，最大特征：{constellationDict[constellation]['最大特征']}，介绍：{constellationDict[constellation]['介绍']}"
# print(mess)