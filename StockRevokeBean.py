# coding=utf-8
from StockBean import StockBean


class StockRevokeBean(StockBean):
    Number_of_transactions = ""  # 成交数量
    Entrustment_number = ""  # 委托数量
    Entrustment_money = ""  # 委托价格
    Average_transaction_price = ""  # 成交均价
    Type = ""  # 操作类型
    Time = ""  # 委托时间
    Day = ""  # 委托日期

    def set_Number_of_transactions(self, s):
        self.Number_of_transactions = s

    def set_Entrustment_number(self, s):
        self.Number_of_transactions = s

    def set_Entrustment_money(self, s):
        self.Number_of_transactions = s

    def set_Average_transaction_price(self, s):
        self.Number_of_transactions = s

    def set_Type(self, s):
        self.Number_of_transactions = s

    def set_Time(self, s):
        self.Number_of_transactions = s

    def set_Day(self, s):
        self.Number_of_transactions = s
