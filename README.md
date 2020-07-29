# Douban-Music-Scrapy

_豆瓣音乐top250排行榜 / 爬虫 / Scrapy框架实现_
_本项目Github链接为_ ___[Douban-Music-Scrapy](https://github.com/MuZeRoFso/Douban-Music-Scrapy)___

---
#### 初步构建Scrapy项目

+ 初始化Scrapy的Spider爬虫

#### 完成爬虫主程序的设计

+ 添加随机请求头(User-agent)的功能
+ 定义items结构
+ 初步设计爬取方式
+ 设计命令行格式化输出

#### 完成数据持久化功能

+ 数据转存至Json文件
+ 数据转存至Excel文件
+ 数据转存至MySQL数据库

#### 完成音乐海报图片下载功能

+ 可将音乐专辑海报保存至本地

#### 拓展功能

+ 实现网页自动翻页的功能
+ 配置上日志系统，将'<u>__DEBUG__</u>'级的信息输出到log文件中
+ 新增数据转存至XML文件功能
+ 成功实现分布式下载。通过动态API获取高匿代理，随机使用代理IP去爬取网页信息

#### 优化程序

> __改进数据转存Json文件模块__
>
> 1. 原版产生Json文件内的Json结构只有第一部分是符合语法的，接下来的都不符合语法
> 2. 因此改进 __`pipelines2json.py`__ 中的数据输入结构，让输出的Json文件内部语法是符合标准的  
> __效果__ : 提升程序执行效率，减少过多的文件 __打开 / 关闭__ 操作  

> __改进项目的`__init.py__`文件:__
>
> 1. 加入Log日志输出文件夹的判定
> 2. 加入output ( json、excel文件保存路径 ) 文件夹的判定
> 3. 加入output/pic ( 图片保存路径 ) 文件夹的判定  
> __效果__ : 不需要在每个pipeline程序中判定对应文件夹是否存在，避免冗余的步骤，也避免重复编码可能带来的错误  

> __添加上延迟抓取功能__  
>
> + 添加 _DOWNLOAD_DELAY_变量，控制爬虫程序请求网页的时间间隔  
> + 添加 _RANDOMIZE_DOWNLOAD_DELAY_ 会令延迟时间更加随机  
> __效果__ : 能稍微提高爬虫程序请求速度过快，避免服务器拒绝服务的情况出现
