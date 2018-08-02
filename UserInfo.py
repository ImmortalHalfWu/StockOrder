# coding=utf-8
class UserInfo(object):

    # 资金余额
    capital_balance = ""
    # 总资产
    total_assets = ""
    # 股票市值
    stock_market_value = ""
    # 可取资金
    advisable_fundse = ""
    # 冻结资金
    frozen_fundse = ""
    # 可用资金
    available_funds = ""
    # 股票持仓
    Stock_holdings = []
    # 可撤销股票
    Stock_revoke = []

    def set_capital_balance(self, s):
        self.capital_balance = s

    def set_total_assets(self, s):
        self.total_assets = s

    def set_stock_market_value(self, s):
        self.stock_market_value = s

    def set_advisable_fundse(self, s):
        self.advisable_fundse = s

    def set_frozen_fundse(self, s):
        self.frozen_fundse = s

    def set_available_funds(self, s):
        self.available_funds = s

    def set_Stock_holdings(self, s):
        # todo 解析持仓数据
        self.Stock_holdings = s

    def set_Stock_revoke(self, s):
        # todo 解析可撤销数据
        self.Stock_revoke = s

    def foo(self):
        pass

SingleUserInfo = UserInfo()