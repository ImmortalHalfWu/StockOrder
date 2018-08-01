# coding=utf-8
from HTMLParser import HTMLParser


import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MyHTMLParser(HTMLParser):

    stockNum = 1        # 股票代码
    buyTime = ""        # 购买时间
    buyStockMoney = 1   # 股票买入单价
    nowStockMoney = 1   # 股票当前单价
    buyNumStart = ""    # 持仓比例起始
    buyNumEnd = ""      # 持仓比例结束
    holdNum = 0         # 持仓数目
    nowMoney = 0        # 当前剩余资金
    index = 0

    def handle_starttag(self, tag, attrs):
        """
        recognize start tag, like <div>
        :param tag:
        :param attrs:
        :return:
        """
        # print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        """
                recognize start tag, like <div>
                :param tag:
                :param attrs:
                :return:
                """
        # print("Encountered a start tag:", tag)

    def handle_data(self, data):
        self.index = self.index + 1
        if self.index == 3:
            varString = "" + data
            self.stockNum = varString[-6:]
        elif self.index == 5:
            self.buyStockMoney = data
        elif self.index == 6:
            self.buyNumStart = data
        elif self.index == 8:
            self.buyNumEnd = data
        elif self.index == 10:
            self.nowStockMoney = data
        elif self.index == 12:
            dataString = "" + data
            self.buyTime = dataString.replace("vartradeTime='", '').replace("';if(tradeTime){$('#tradeTime').text(tradeTime);}", '')


    def handle_startendtag(self, tag, attrs):
        """
        recognize tag that without endtag, like <img />
        :param tag:
        :param attrs:
        :return:
        """
        print("Encountered startendtag :", tag)

    def handle_comment(self, data):
        """

        :param data:
        :return:
        """
        print("Encountered comment :", data)

