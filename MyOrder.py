# coding=utf-8
import win32gui
import time

import win32con
from pandas import json

import KeyBroadUtil
import log
from Util import SingleUtil
from UserInfoBean import SingleUserInfo


class MyOrder:

    def __init__(self):
        self.keyBroadUtil = KeyBroadUtil.KeyBrodaUtil()
        self.xiadanH = SingleUtil.findMainHwnd()
        if self.xiadanH == 0:
            log.log("3s后重新尝试")
            time.sleep(3000)
            self.xiadanH = SingleUtil.findMainHwnd()
        if self.xiadanH != 0:
            # todo 初始化用户数据
            self.initUserInfo()

    def clickBroad(self, VK):
        self.keyBroadUtil.clickBroad(VK)

    def clickBroadF2(self):
        self.clickBroad(win32con.VK_F2)

    def clickBroadF1(self):
        self.clickBroad(win32con.VK_F1)

    def clickBroadF4(self):
        self.clickBroad(win32con.VK_F4)

    def clickTab(self, clickNum):
        self.keyBroadUtil.clickTab(clickNum)

    def clickEnter(self, ):
        self.keyBroadUtil.clickEnter()

    def sell(self, stockNum, sellNum):
        win32gui.SetForegroundWindow(self.xiadanH)
        self.clickBroadF1()
        self.clickBroadF2()
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
        self.clickBroadF2()
        self.clickBroadF1()
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

    def initUserInfo(self):
        log.log("===================================================")
        log.log("开始填充用户数据.......")
        log.log("===================================================")
        # 程序前置
        win32gui.SetForegroundWindow(self.xiadanH)
        self.clickBroadF2()
        self.clickBroadF4()
        childWindows = SingleUtil.findChildWindows(self.xiadanH)
        for childHw in childWindows:
            # title = show_window_attr(h)
            windowTitle = SingleUtil.getWindowText(childHw)
            # log.log '窗口标题:%s' % (str(title))
            if "资金余额" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_capital_balance(findTitle)
            if "总 资 产" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_total_assets(findTitle)
            if "股票市值" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_stock_market_value(findTitle)
            if "可取金额" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_advisable_fundse(findTitle)
            if "冻结金额" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_frozen_fundse(findTitle)
            if "可用金额" in str(windowTitle):
                findTitle = self.find_text_for_index(childWindows, childHw)
                SingleUserInfo.set_available_funds(findTitle)

        SingleUserInfo.__dict__ = json.loads(json.dumps(SingleUserInfo.__dict__).replace("\u0000", ""))
        log.log("===================================================")
        log.log("用户信息资金信息：")
        log.log(json.dumps(SingleUserInfo.__dict__))
        log.log("===================================================")

    def find_text_for_index(self, hWndList, h):
        index = hWndList.index(h) + 3
        findTitle = SingleUtil.getWindowText(hWndList[index])
        return findTitle