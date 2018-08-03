# coding=utf-8
import json
import urllib
import urllib2
import time

import FileUtil
import log
from MyHTMLParser import MyHTMLParser
import MyOrder as myOrder

#################################################获取大神交易记录

# def printUserInfo():
#     # 获取当前持仓状态
#     arrAccountInfo = ["总资产", "可用资金", "持仓总市值", "总盈利金额", "持仓数量"];
#     for i in range(0, len(arrAccountInfo)):
#         value = GetAccountInfo(u"", i, 0)
#         print ("%s %f " % (arrAccountInfo[i], value))
#     print '--------------------------------------------------------'
#     # 取出所有的持仓股票代码,结果以 ','隔开的
#     allStockCode = GetAllPositionCode(0)
#     allStockCodeArray = allStockCode.split(',')
#     for i in range(0, len(allStockCodeArray)):
#         vol = GetPosInfo(allStockCodeArray[i], 0, 0)
#         changeP = GetPosInfo(allStockCodeArray[i], 4, 0)
#         print '持仓股票:'
#         print ("%s %d %.2f%%" % (allStockCodeArray[i], vol, changeP))
#     print '--------------------------------------------------------'


def printStockInfo(htmlParser):
    log.log("股票代码" + htmlParser.stockNum)
    log.log("成交价" + htmlParser.buyStockMoney)
    log.log("持仓比例" + htmlParser.buyNumStart + "-->" + htmlParser.buyNumEnd)
    log.log("此股票当前价" + htmlParser.nowStockMoney)
    log.log("此次购买时间为" + htmlParser.buyTime)

while int(time.strftime('%H%M',time.localtime(time.time()))) < 928 :
    time.sleep(30)

log.log("当前时间：" + time.strftime('%H%M',time.localtime(time.time())))
log.log("开始查询......")

var = 0
while var < 2:  # 该条件永远为true，循环将无限执行下去
    # try:

        data1 = {
            'pin': 'jd_743bd4112ba1e'
        }

        data = urllib.urlencode(data1)
        req = urllib2.Request('http://gupiao.jd.com/package/lastConverts', urllib.urlencode(data1))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        req.add_header('Referer', 'http://gupiao.jd.com/find/12195')
        req.add_header('Host', 'gupiao.jd.com')
        req.add_header('Origin', 'http://gupiao.jd.com')
        req.add_header('Cookie',
                       'TrackID=1zjctpUkfXiPPpd2-FlJw52fq9gkx9v0WGqH_4sECdaGDpJ8D_58Bqx-Bx4HQsVMYTsT5X4AEec9ZtKVXPzJEMA; pinId=EX7C17pLL2_bXrUjzBWQTQ; __jdv=204210054|direct|-|none|-|1531620946230; _jrda=3; sec_flag=e125e94ccd30d095203da363b24adad3; sec_addr=c0a8006c; wlfstk_smdl=uj4fvqhhhqq66p2ddnrgf4vw8a2cggkb; 3AB9D23F7A4B3C9B=XG5I3N4FBWQZLN7HPAC56MKB755NV4K4D6CA6ICAOGCMBJBKMFJPJFYCRFOUFX7YP4IHFLD3YJJESRXWWTFXSHEVFM; __jda=204210054.1495960752486274042302.NaN.1525092662.1531620946.23; __jdb=204210054.10.1495960752486274042302|23.1531620946; __jdc=204210054; __jdu=1495960752486274042302; _jrdb=1531621024187')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        response = urllib2.urlopen(req)
        string = response.read().replace("\n", "").replace("\t", "").replace(" ", "").replace("%", "")
        # print string
        htmlParser = MyHTMLParser()
        htmlParser.feed(string)

        # 对象转Json
        parserDict = htmlParser.__dict__

        try:
            parserDict.pop('interesting')
            parserDict.pop('lasttag')
            parserDict.pop('lineno')
            parserDict.pop('offset')
            parserDict.pop('cdata_elem')
            parserDict.pop('rawdata')
            parserDict.pop('_HTMLParser__starttag_text')
            parserDict.pop('index')
            # parserDict['buyNumStart'] = "100.00"
            # parserDict['buyNumEnd'] = "0.00"
        except Exception, e:
            log.log(e.message)

        # 当前最新数据
        parserJson = json.dumps(parserDict)

        # 本地最近数据
        fileUtil = FileUtil.FileUtil()
        newStock = fileUtil.readNewStock()
        jsonToDict = json.loads(newStock)
        myNewParser = MyHTMLParser()
        myNewParser.__dict__ = jsonToDict

        # 两次时间比较,如果不相同，则下单
        if myNewParser.buyTime != htmlParser.buyTime:
            log.log(
                '================================================================================================================')
            mOrderUtill = myOrder.MyOrder()
            var = var + 1
            # 开始新的交易，卖出还是买入
            if htmlParser.buyNumStart > htmlParser.buyNumEnd:  # 卖出
                # 计算卖出%比，取出目前此股票持仓，按百分比计算卖出的数目，卖出
                stockVol = myNewParser.holdNum
                # mOrderUtill.sell(htmlParser.stockNum, int(stockVol), float(htmlParser.nowStockMoney))
                mOrderUtill.sell(htmlParser.stockNum, stockVol)
                log.log("卖出: %s，当前持有数量：%s,卖出价格：%s" % (htmlParser.stockNum, stockVol, htmlParser.nowStockMoney))
                parserDict['holdNum'] = "0"
                parserDict['nowMoney'] = str(float(htmlParser.nowStockMoney) * int(stockVol) + float(myNewParser.nowMoney))
            else:  # 买入
                # 计算买入%比，取出目前剩余资金，按百分比计算买入此股票，卖出
                useableMoney = float(myNewParser.nowMoney)
                buyNum = useableMoney / float(htmlParser.nowStockMoney)
                # buyNum = 1024 / float(htmlParser.nowStockMoney)
                if (buyNum > 100):
                    buyNum = int(buyNum) / 100 * 100
                    mOrderUtill.buy(htmlParser.stockNum, str(buyNum))
                    parserDict['holdNum'] = str(buyNum)
                    parserDict['nowMoney'] = useableMoney - buyNum * float(htmlParser.nowStockMoney)
                else:
                    log.log("取消此次交易")
                    log.log ("买入: %s，余额：%s,买入价格：%s,买入份额：%s" % (
                        htmlParser.stockNum, useableMoney, htmlParser.nowStockMoney, buyNum))
                    break

                log.log ("买入: %s，余额：%s,买入价格：%s,买入份额：%s" % (
                htmlParser.stockNum, useableMoney, htmlParser.nowStockMoney, buyNum))

            parserJson = json.dumps(parserDict)
            fileUtil.writeStock(parserJson)  # 写入最近一次交易
            log.log ("网页数据为: %s" % (parserJson))
            log.log ("本地数据为: %s" % (newStock))
            log.log("当前时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            # printUserInfo()
            # printStockInfo(htmlParser)

        time.sleep(1)

    # except Exception, e:
    #     print e.message