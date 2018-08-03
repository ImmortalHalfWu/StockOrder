import OrderUtil as mOrder
import log

saf = mOrder.OrderUtill()
dd = """
    网页解析拿到最新数据
    得到目标编号，持仓变化
    if 持仓增加，则买
        1，取出目标单价
        2，取出目前可用金额
        3，buyNum = 可用金额/目标单价
        4，if buyNum > 0 调用API下单
    else 持仓减少，则卖
        1，根据编号， 取出当前持有股数
        2，如果股数>0，调用API下单
"""
log.log(saf.getUseableMoney())
log.log(saf.findStockVol('002232'))