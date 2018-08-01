# coding=utf-8
import win32api
import win32process

import win32clipboard as mWin32clipboard

import win32con
import win32gui
import psutil
import time
import MyOrder as myOrder


def find_idxSubHandle(pHandle, winClass, index=0):
    """
                已知子窗口的窗体类名
                寻找第index号个同类型的兄弟窗口
    """
    assert type(index) == int and index >= 0
    handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
    while index > 0:
        handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
        index -= 1
    return handle


def find_subHandle(pHandle, winClassList):
    """
        递归寻找子窗口的句柄
        pHandle是祖父窗口的句柄
        winClassList是各个子窗口的class列表，父辈的list-index小于子辈
    """
    assert type(winClassList) == list
    if len(winClassList) == 1:
        return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
    else:
        pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        return find_subHandle(pHandle, winClassList[1:])


"""输出phandle的所有子控件"""


def p_sub_handle(phandle):
    handle = -1
    while handle != 0:
        if handle == -1:
            handle = 0
        handle = win32gui.FindWindowEx(phandle, handle, None, None)
        if handle != 0:
            className = win32gui.GetClassName(handle)
            print(className)


def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


def utf8toGbk(s):
    return s.decode('utf-8').encode('gbk')


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
            return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def findProcessByName(name):
    # 通过进程名称获取窗口句柄并前置
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == name:
            hwnds = get_hwnds_for_pid(pid)
            return hwnds[0]


def clickBroad(VK):
    win32api.keybd_event(VK, 0, 0, 0)
    win32api.keybd_event(VK, 0, win32con.KEYEVENTF_KEYUP, 0)


def clickTab(clickNum):
    i = 1
    while i <= clickNum:
        clickBroad(win32con.VK_TAB)
        i += 1


def clickEnter():
    clickBroad(win32con.VK_RETURN)

def sell(stockNum, sellNum):
    clickBroad(win32con.VK_F1)
    clickBroad(win32con.VK_F2)
    # 4下tab
    clickTab(4)

    # enter确定重填
    clickEnter()
    # 卖出股票
    stockNums = map(ord, stockNum)
    for index in stockNums:
        clickBroad(index)

    clickTab(2)
    # 卖出份额
    sellNums = map(ord, sellNum)
    for index in sellNums:
        clickBroad(index)
    time.sleep(0.2)
    clickBroad(KEY_S)
    clickEnter()
    time.sleep(0.2)
    clickEnter()

def buy(stockNum, buyNum):

    clickBroad(win32con.VK_F2)
    clickBroad(win32con.VK_F1)
    # 4下tab
    clickTab(4)

    # enter确定重填
    clickEnter()
    # 买入股票
    stockNums = map(ord, stockNum)
    for index in stockNums:
        clickBroad(index)

    clickTab(2)
    # 买入份额
    buyNums = map(ord, buyNum)
    for index in buyNums:
        clickBroad(index)
    time.sleep(0.2)
    clickBroad(KEY_B)
    clickBroad(KEY_Y)


KEY_B = 66
KEY_Y = 89
KEY_S = 83
# xiadanH = findProcessByName("xiadan.exe")
xiadan = win32gui.FindWindow(None, utf8toGbk("网上股票交易系统5.0"))
# p_sub_handle(xiadan)
editHandle = find_subHandle(xiadan, [("Static",0)])
# editHandle = win32gui.FindWindowEx(xiadan, None, "Static", None)
# title = utf8toGbk(win32gui.GetWindowText(xiadan))
# clsname = win32gui.GetClassName(xiadan)
print ("%x" % (editHandle))

# 通过读取Static控件可以获得账户资金情况
text = win32gui.GetWindowText(199814)
print(gbk2utf8(text))


# mOrderUtill = myOrder.MyOrder()
# mOrderUtill.buy("300607","100")
# 程序前置
# win32gui.SetForegroundWindow(xiadanH)
# sell("300607", "100")
# win32gui.SetBkMode(xiadanH, win32con.TRANSPARENT)

# p_sub_handle(xiadanH)

# sss1 = map(ord,"1000")
# for index in sss1 :
#     win32api.keybd_event(index, 0, 0, 0)
#     win32api.keybd_event(index, 0, win32con.KEYEVENTF_KEYUP, 0)

# # 内容填充值剪切板
# mWin32clipboard.OpenClipboard()
# mWin32clipboard.EmptyClipboard()
# mWin32clipboard.SetClipboardData(win32con.CF_TEXT, "123123")
# mWin32clipboard.CloseClipboard()
# # 快捷键粘贴
# win32api.keybd_event(17, 0, 0, 0)                           # ctrl的键位码是17
# win32api.keybd_event(86, 0, 0, 0)                           # v的键位码是86
# win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)    # 释放按键
# win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

# 按下F5
# win32api.keybd_event(116, 0, 0, 0)
# # 松开F5
# win32api.keybd_event(116, 0, win32con.KEYEVENTF_KEYUP, 0)
# # 按下F1
# win32api.keybd_event(112, 0, 0, 0)
# # 松开F1
# win32api.keybd_event(112, 0, win32con.KEYEVENTF_KEYUP, 0)

# notepadH = win32gui.FindWindow(None, utf8toGbk("网上股票交易系统5.0"))
# print(notepadH)

# p_sub_handle(notepadH)
# editH = find_subHandle(notepadH, [("Edit",0)])
# print(editH)

# 获取所有子控件句柄
# hWndChildList = []
# win32gui.EnumChildWindows(notepadH, lambda hWnd, param: param.append(hWnd), hWndChildList)
# for h in hWndChildList:
#     title = win32gui.GetWindowText(h)
#     title = gbk2utf8(title)
#     clsname = win32gui.GetClassName(h)
#     print '窗口句柄:%s ' % (h)
#     print '窗口标题:%s' % (title)
#     print '窗口类名:%s' % (clsname)
#     print ''
