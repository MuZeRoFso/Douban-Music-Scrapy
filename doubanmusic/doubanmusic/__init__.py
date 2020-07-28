import os

# 日志文件夹
LogDir = 'Log'
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(LogDir):
    os.mkdir(LogDir)

# Json、Excel输出文件夹
DataDir = 'output'
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(DataDir):
    os.mkdir(DataDir)

# 图片文件夹
PicDir = 'output/pic'
# 判断该文件夹是否存在，不存在则创建
if not os.path.exists(PicDir):
    os.mkdir(PicDir)
