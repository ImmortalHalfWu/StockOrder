# coding=utf-8
import time
import win32api
import win32gui
import win32process

import psutil
import win32con
from win32con import WM_KEYDOWN, VK_RETURN

import Util

import MyOrder


def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


def utf8toGbk(s):
    return s.decode('utf-8').encode('gbk')


# mUtil = Util.SingleUtil
#
# mainHwnd = mUtil.findMainHwnd

mOrder = MyOrder.MyOrder()

# 查询



# todo 向窗口发送按键指令
win32gui.SendMessage(mOrder.xiadanH, WM_KEYDOWN, win32con.VK_F1, 0)
time.sleep(1000)
win32gui.SendMessage(mOrder.xiadanH, WM_KEYDOWN, win32con.VK_F2, 0)
time.sleep(1000)
win32gui.SendMessage(mOrder.xiadanH, WM_KEYDOWN, win32con.VK_F3, 0)
time.sleep(1000)

win32gui.SendMessage(mOrder.xiadanH, WM_KEYDOWN, win32con.VK_F4, 0)
time.sleep(1000)

# SendMessage(hWnd, WM_KEYUP, VK_RETURN, 0);