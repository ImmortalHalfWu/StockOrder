# -*- coding: UTF-8 -*-
import os

class FileUtil:

    lineBetween = "-----------------------------------------------"
    mFile = None
    fileName = "jiao_yi_ji_lv.txt"
    fileMode = 'a+'

    def writeStock(self, jsonString):
        self.mFile = open(self.fileName, self.fileMode)
        # self.mFile.write('\n'+self.lineBetween+')
        self.mFile.write('\n' + jsonString)
        # timer = self.mFile.readline()
        # print(timer)
        self.mFile.close()

    def readNewStock(self):
        self.mFile = open(self.fileName, self.fileMode)
        lastJson = ''
        for lastJson in self.mFile.readlines():  # 依次读取每行
            lastJson = lastJson.strip()  # 去掉每行头尾空白
            # print "读取的数据为: %s" % (line)
        self.mFile.close()
        return lastJson

# fileUtil = FileUtil()
# fileUtil.writeStock("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"+'\n')
# fileUtil.writeStock("21111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112"+'\n')
# fileUtil.writeStock("31111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111113"+'\n')
# fileUtil.readNewStock()
# fileUtil.writeStock("41111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111114"+'\n')
