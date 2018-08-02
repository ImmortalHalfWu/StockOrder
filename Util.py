# coding=utf-8
import win32gui
import win32process

import psutil
import win32con
import win32clipboard as win32clipboard

'''
工具类
'''


class Util():
    '''
    gbk 转 utf
    '''

    def gbk2utf8(sele, s):
        return s.decode('gbk').encode('utf-8')

    '''
    utf 转 gbk
    '''

    def utf8toGbk(sele, s):
        return s.decode('utf-8').encode('gbk')

    '''
    查找交易软件句柄
    '''

    def findMainHwnd(self):
        print("开始查找主程序....")
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
                            print("查找主程序成功....")
                            print(self.gbk2utf8(win32gui.GetWindowText(hwnd)))
                            print(hwnd, processId)
                            return hwnd
        return 0

    '''
    获取控件文本
    '''

    def getWindowText(self, hWnd):
        print("获取控件text：%s" %(hWnd))
        # 空返回
        if not hWnd:
            return ""

        clsname = win32gui.GetClassName(hWnd)
        len = win32gui.SendMessage(hWnd, win32con.WM_GETTEXTLENGTH) + 1  # 获取edit控件文本长度
        buffer = '0' * len
        win32gui.SendMessage(hWnd, win32con.WM_GETTEXT, len, buffer)  # 读取文本
        # 中文系统默认title是gb2312的编码
        title = self.gbk2utf8(buffer)
        print '窗口句柄:%s ' % (self.gbk2utf8(str(hWnd)))
        print '窗口标题:%s' % (title)
        print '窗口类名:%s' % (clsname)
        return title

    '''
    读取剪切板
    '''

    def readCopyText(self):
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
        win32clipboard.CloseClipboard()
        print("读取剪切板内容：" + text)
        return text

    '''
    向剪切板中添加数据
    '''

    def setCopyText(self, text):
        print("写入剪切板内容：" + text)
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TEXT, text)
        win32clipboard.CloseClipboard()
