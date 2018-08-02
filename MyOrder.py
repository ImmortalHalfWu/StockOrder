# coding=utf-8
import win32gui
import time

import win32con

import KeyBroadUtil
import Util


class MyOrder:

    def __init__(self):
        self.util = Util.Util()
        self.keyBroadUtil = KeyBroadUtil.KeyBrodaUtil()
        self.xiadanH = self.util.findMainHwnd()

    def clickBroad(self, VK):
        self.keyBroadUtil.clickBroad(VK)

    def clickTab(self, clickNum):
        self.keyBroadUtil.clickTab(clickNum)

    def clickEnter(self, ):
        self.keyBroadUtil.clickEnter()

    def sell(self, stockNum, sellNum):
        win32gui.SetForegroundWindow(self.xiadanH)
        self.clickBroad(win32con.VK_F1)
        self.clickBroad(win32con.VK_F2)
        # 4下tab
        self.clickTab(4)

        # enter确定重填
        self.clickEnter()
        # 卖出股票
        stockNums = map(ord, stockNum)
        for index in stockNums:
            self.clickBroad(index)

        self.clickTab(2)
        # 卖出份额
        sellNums = map(ord, sellNum)
        for index in sellNums:
            self.clickBroad(index)
        time.sleep(0.2)
        self.clickBroad(self.keyBroadUtil.KEY_S)
        self.clickEnter()
        time.sleep(0.2)
        self.clickEnter()

    def buy(self, stockNum, buyNum):
        # 程序前置
        win32gui.SetForegroundWindow(self.xiadanH)
        self.clickBroad(win32con.VK_F2)
        self.clickBroad(win32con.VK_F1)
        # 4下tab
        self.clickTab(4)

        # enter确定重填
        self.clickEnter()
        # 买入股票
        stockNums = map(ord, stockNum)
        for index in stockNums:
            self.clickBroad(index)

        self.clickTab(2)
        # 买入份额
        buyNums = map(ord, buyNum)
        for index in buyNums:
            self.clickBroad(index)
        time.sleep(0.2)
        self.clickBroad(self.keyBroadUtil.KEY_B)
        self.clickBroad(self.keyBroadUtil.KEY_Y)

    # xiadanH = findProcessByName("xiadan.exe")
    # 程序前置
    # win32gui.SetForegroundWindow(xiadanH)
    # sell("300607", "100")
    # win32gui.SetBkMode(xiadanH, win32con.TRANSPARENT)
