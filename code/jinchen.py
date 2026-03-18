from subprocess import Popen
import psutil
import os


def openOneTxt(path):
    if os.path.exists(path) and path.endswith('.txt'):
        Popen(['notepad.exe', path])


def openManyTxt(paths):
    for path in paths:
        openOneTxt(path)


def closeAllTxt():
    for p in psutil.process_iter():
        if p.name().lower() == 'notepad.exe':
            p.terminate()


import time

paths = ['红楼梦\\第001回.txt',
         '红楼梦\\第002回.txt',
         '红楼梦\\第003回.txt',
         '红楼梦\\第004回.txt']
openManyTxt(paths)
time.sleep(3)
closeAllTxt()