import os

# 日志文件夹
LogDir = 'Log'
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(LogDir):
    os.mkdir(LogDir)
