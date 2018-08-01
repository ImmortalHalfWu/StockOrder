# coding=utf-8
#股票自动交易助手 Python 自动下单使用 例子
#把此脚本和 StockOrderApi.py Order.dll 放到你自己编写的脚本同一目录
from StockOrderApi import *

class OrderUtill :
    def buy(self, stockNum, buyNum, buyMoney):
        Buy(stockNum, buyNum, buyMoney, 1, 0)

    def sell(self, stockNum, sellNum, sellMoney):
        Sell(stockNum, sellNum, sellMoney, 1, 0)

    # 获取指定股票持仓数目
    def findStockVol(self, stockNum):
        allStockCode = GetAllPositionCode(0)
        allStockCodeArray = allStockCode.split(',')
        for i in range(0, len(allStockCodeArray)):
            if stockNum == allStockCodeArray[i]:
                num = GetPosInfo(allStockCodeArray[i], 0, 0)
                if num is None:
                    return 0
                return num
        return 0

    # 获取可用剩余资金
    def getUseableMoney(self):
        return GetAccountInfo(u"", 1, 0)