# coding=utf-8
import win32con
from pandas import json

import log
from UserInfoBean import SingleUserInfo
import test
from Util import SingleUtil

__author__ = 'Administrator'

__doc__ = '''
pythonwin中win32gui的用法
本文件演如何使用win32gui来遍历系统中所有的顶层窗口，
并遍历所有顶层窗口中的子窗口
'''

import win32gui
from pprint import pprint


def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


def utf8toGbk(s):
    return s.decode('utf-8').encode('gbk')


def show_window_attr(hWnd):
    '''
    显示窗口的属性
    :return:
    '''
    if not hWnd:
        return

    clsname = win32gui.GetClassName(hWnd)

    len = win32gui.SendMessage(hWnd, win32con.WM_GETTEXTLENGTH) + 1  # 获取edit控件文本长度
    buffer = '0' * len
    win32gui.SendMessage(hWnd, win32con.WM_GETTEXT, len, buffer)  # 读取文本
    # 中文系统默认title是gb2312的编码
    title = gbk2utf8(buffer)

    log.log ('窗口句柄:%s ' % (gbk2utf8(str(hWnd))))
    log.log ('窗口标题:%s' % (title))
    log.log ('窗口类名:%s' % (clsname))
    log.log ('')
    return title


def show_windows(hWndList):
    for h in hWndList:
        # title = show_window_attr(h)
        windowTitle = mUtil.getWindowText(h)
        # log.log '窗口标题:%s' % (str(title))
        if "资金余额" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_capital_balance(findTitle)
        if "总 资 产" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_total_assets(findTitle)
        if "股票市值" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_stock_market_value(findTitle)
        if "可取金额" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_advisable_fundse(findTitle)
        if "冻结金额" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_frozen_fundse(findTitle)
        if "可用金额" in str(windowTitle):
            findTitle = find_text_for_index(hWndList, h)
            SingleUserInfo.set_available_funds(findTitle)

    SingleUserInfo.__dict__ = json.loads(json.dumps(SingleUserInfo.__dict__).replace("\u0000", ""))
    log.log(json.dumps(SingleUserInfo.__dict__))


def find_text_for_index(hWndList, h):
    index = hWndList.index(h) + 3
    findTitle = mUtil.getWindowText(hWndList[index])
    return findTitle


def demo_top_windows():
    '''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    show_windows(hWndList)

    return hWndList


def demo_child_windows(parent):
    '''
    演示如何列出所有的子窗口
    :return:
    '''
    if not parent:
        return

    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWndChildList)
    show_windows(hWndChildList)
    return hWndChildList


mUtil = SingleUtil
xiadan = win32gui.FindWindow(None, utf8toGbk("网上股票交易系统5.0"))
demo_child_windows(xiadan)

# hWndList = demo_top_windows()
# assert len(hWndList)
#
# parent = hWndList[20]
# # 这里系统的窗口好像不能直接遍历，不知道是否是权限的问题
# hWndChildList = demo_child_windows(parent)
#
# log.log('-----top windows-----')
# plog.log(hWndList)
#
# log.log('-----sub windows:from %s------' % (parent))
# plog.log(hWndChildList)
