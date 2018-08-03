# coding=utf-8
import win32api
import win32gui
import win32process

import psutil

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


