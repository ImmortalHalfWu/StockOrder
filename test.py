# coding=utf-8
import win32api
import win32gui
import win32process

import psutil

def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')


def utf8toGbk(s):
    return s.decode('utf-8').encode('gbk')

# 遍历所有进程取得pid
# 通过pid获取进程名称
# 如果进程名称匹配
# 通过pid获取句柄


hwndList = []
# 获取所有窗口句柄
win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwndList)
# 遍历所有窗口
for hwnd in hwndList:
    threadId, processId = win32process.GetWindowThreadProcessId(hwnd)
    # print(hwnd,processId)

pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    if p.name() == "xiadan.exe":
        print(p.name()+"__" + str(p.pid))
        hwndList = []
        # 获取所有窗口句柄
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwndList)
        # 遍历所有窗口
        for hwnd in hwndList:
            threadId, processId = win32process.GetWindowThreadProcessId(hwnd)
            if pid == processId:
                title = gbk2utf8(win32gui.GetWindowText(hwnd))
                if title == "网上股票交易系统5.0" or "网上股票" in title or "股票交易" in title or "交易系统" in title or "系统5.0" in title:
                    print(gbk2utf8(win32gui.GetWindowText(hwnd)))
                    print( hwnd, processId)