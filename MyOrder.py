# coding=utf-8
import win32api
import win32process
import win32con
import win32gui
import psutil
import time

class MyOrder:

    def __init__(self):
        self.xiadanH = win32gui.FindWindow(None, self.utf8toGbk("网上股票交易系统5.0"))
        # self.xiadanH = self.findProcessByName("xiadan.exe")

    def utf8toGbk(self,s):
        return s.decode('utf-8').encode('gbk')

    def get_hwnds_for_pid(self, pid):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    hwnds.append(hwnd)
                return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds

    def findProcessByName(self,name):
        # 通过进程名称获取窗口句柄并前置
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if p.name() == name:
                hwnds = self.get_hwnds_for_pid(pid)
                return hwnds[0]

    def clickBroad(self,VK):
        win32api.keybd_event(VK, 0, 0, 0)
        win32api.keybd_event(VK, 0, win32con.KEYEVENTF_KEYUP, 0)

    def clickTab(self,clickNum):
        i = 1
        while i <= clickNum:
            self.clickBroad(win32con.VK_TAB)
            i += 1

    def clickEnter(self,):
        self.clickBroad(win32con.VK_RETURN)

    def sell(self,stockNum, sellNum):
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
        self.clickBroad(self.KEY_S)
        self.clickEnter()
        time.sleep(0.2)
        self.clickEnter()

    def buy(self,stockNum, buyNum):
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
        self.clickBroad(self.KEY_B)
        self.clickBroad(self.KEY_Y)

    KEY_B = 66
    KEY_Y = 89
    KEY_S = 83
    KEY_C = 67
    KEY_V = 86
    # xiadanH = findProcessByName("xiadan.exe")
    # 程序前置
    # win32gui.SetForegroundWindow(xiadanH)
    # sell("300607", "100")
    # win32gui.SetBkMode(xiadanH, win32con.TRANSPARENT)