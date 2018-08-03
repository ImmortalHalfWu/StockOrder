# coding=utf-8
import win32api
import win32process
import win32con
import win32gui
import psutil
import time

import log

'''
键盘相关工具
'''
class KeyBrodaUtil():

    KEY_B = 66
    KEY_Y = 89
    KEY_S = 83
    KEY_C = 67
    KEY_V = 86

    def clickBroad(self, VK):
        win32api.keybd_event(VK, 0, 0, 0)
        win32api.keybd_event(VK, 0, win32con.KEYEVENTF_KEYUP, 0)

    def clickTab(self, clickNum):
        log.log("输入" + str(clickNum) + "下TAB键")
        i = 1
        while i <= clickNum:
            self.clickBroad(win32con.VK_TAB)
            i += 1

    def clickEnter(self):
        log.log("输入Enter键")
        self.clickBroad(win32con.VK_RETURN)


    def clickCopy(self):
        log.log("输入Copy操作")
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(67, 0, 0, 0)
        win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)

    def clickPaste(self):
        log.log("输入Paset操作")
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)