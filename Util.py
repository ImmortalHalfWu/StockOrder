# coding=utf-8
import win32gui
import win32process

import psutil
import win32con
import win32clipboard as win32clipboard

import log

'''
工具类
'''


class Util():

    def gbk2utf8(sele, s):

        '''
        gbk 转 utf
        '''
        return s.decode('gbk').encode('utf-8')

    def utf8toGbk(sele, s):
        '''
        utf 转 gbk
        '''
        return s.decode('utf-8').encode('gbk')

    def findMainHwnd(self):
        '''
        查找交易软件句柄
        '''
        try:
            log.log("开始查找主程序....")
            processName = "xiadan.exe"
            pids = psutil.pids()
            for pid in pids:
                p = psutil.Process(pid)
                if p.name() == processName:
                    hwndList = []
                    # 获取所有窗口句柄
                    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwndList)
                    # 遍历所有窗口
                    for hwnd in hwndList:
                        threadId, processId = win32process.GetWindowThreadProcessId(hwnd)
                        if pid == processId:
                            title = self.gbk2utf8(win32gui.GetWindowText(hwnd))
                            # 通过标题判断
                            if title == "网上股票交易系统5.0" or "网上股票" in title or "股票交易" in title or "交易系统" in title or "系统5.0" in title:
                                log.log("查找主程序成功....")
                                log.log(self.gbk2utf8(win32gui.GetWindowText(hwnd)))
                                return hwnd
        except Exception as e:
            log.log("主程序查找失败 ： " + e.message)

        return 0


    def getWindowText(self, hWnd):
        '''
        获取控件文本
        '''
        log.log("获取控件text：%s" % (hWnd))
        # 空返回
        if not hWnd:
            return ""

        clsname = win32gui.GetClassName(hWnd)
        len = win32gui.SendMessage(hWnd, win32con.WM_GETTEXTLENGTH) + 1  # 获取edit控件文本长度
        buffer = '0' * len
        win32gui.SendMessage(hWnd, win32con.WM_GETTEXT, len, buffer)  # 读取文本
        # 中文系统默认title是gb2312的编码
        title = self.gbk2utf8(buffer)
        log.log('窗口句柄:%s ' % (self.gbk2utf8(str(hWnd))))
        log.log('窗口标题:%s' % (title))
        log.log('窗口类名:%s' % (clsname))
        return title


    def findChildWindows(self, parent):
        '''
        获取指定窗口的所有的子窗口
        '''
        if not parent:
            return

        hWndChildList = []
        win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWndChildList)
        return hWndChildList


    def readCopyText(self):
        '''
        读取剪切板
        '''
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
        win32clipboard.CloseClipboard()
        log.log("读取剪切板内容：" + text)
        return text


    def setCopyText(self, text):
        '''
        向剪切板中添加数据
        '''
        log.log("写入剪切板内容：" + text)
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TEXT, text)
        win32clipboard.CloseClipboard()


SingleUtil = Util()
