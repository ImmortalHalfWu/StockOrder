# coding=utf-8
class StockBean:

    stockNum = ""       # 股票号码
    stockName = ""      # 股票名称
    stockBalance = ""   # 股票余额
    stockFunds = ""     # 可用余额
    stockFrozen = ""    # 冻结数量
    stockProfitLoss = ""# 股票盈亏
    stockCostPrice = "" # 成本价
    stockProfitLossRatio = ""   # 盈亏比
    stockMarketValue = "" # 市值


    def setStockNum(self, stockNum):
        self.stockNum = stockNum

    def setstockName(self, stockName):
        self.stockName = stockName

    def setstockBalance(self, stockBalance):
        self.stockBalance = stockBalance

    def setstockFunds(self, stockFunds):
        self.stockFunds = stockFunds

    def setstockFrozen(self, stockFrozen):
        self.stockFrozen = stockFrozen

    def setstockProfitLoss(self, stockProfitLoss):
        self.stockProfitLoss = stockProfitLoss

    def setstockCostPrice(self, stockProfitLossRatio):
        self.stockProfitLossRatio = stockProfitLossRatio

    def setstockMarketValue(self, stockMarketValue):
        self.stockMarketValue = stockMarketValue




