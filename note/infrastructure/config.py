import os
import sys

DEBUG = True

APP_NAME = 'note'

# 工作空间下的文件夹
APP_DATE_DIR_NAME = '.NOTE'
TASK_DIR_NAME = 'TASK'
PURGE_DIR_NAME = 'PURGE'

# 工作空间下的文件
DB_PATH = os.path.join(APP_DATE_DIR_NAME, 'note.db3')
LOG_PATH = os.path.join(APP_DATE_DIR_NAME, 'log.txt')
CONFIG_PATH = os.path.join(APP_DATE_DIR_NAME, 'conf.txt')
IGNORE_PATH = os.path.join(APP_DATE_DIR_NAME, 'ignore.txt')

# 处理过程中忽略的文件
IGNORE_FILES = (
    APP_DATE_DIR_NAME + os.sep, TASK_DIR_NAME + os.sep, PURGE_DIR_NAME + os.sep)
if DEBUG:
    IGNORE_FILES += ('*.py', '__pycache__/', '.git/', '*.exe', '*.lnk')

_DIR_PATH = os.path.dirname(__file__)

# 程序用到的一些数据文件,位置会随打包而变动
if DEBUG:
    LOCALES = os.path.join(_DIR_PATH, 'locales')
    DOC_PATH = os.path.join(_DIR_PATH, '../../docs/使用说明.rst')
else:
    # 使用PyInstaller打包后frozen为True,且_MEIPASS为数据目录
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        LOCALES = os.path.join(sys._MEIPASS, 'locales')
        DOC_PATH = os.path.join(sys._MEIPASS, 'docs/使用说明.rst')
