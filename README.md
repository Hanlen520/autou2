# 需求背景

自动化测试详情页分享到微信,验证分享到微信页面的h5页面是否正确 可以脱离pc运行.

技术实现基于python-uiautomator2 + atx-agent + qpython.


## 环境搭建

# qpython下载
```
https://github.com/qpython-android/qpython/releases
```
adb install Qpython_2018-12-31_cn.apk


# uiautomator2
pip install --pre uiautomator2

# git下载源码安装
git clone https://github.com/openatx/uiautomator2
pip install -e uiautomator2

# 安装pillow依赖,图片库
pip install pillow

# 手机安装

电脑连接上一个手机或多个手机, 确保adb已经添加到环境变量中，

执行下面的命令会自动安装本库所需要的设备端程序:

```
uiautomator-server 、atx-agent、openstf/minicap、openstf/minitouch
```
```
python -m uiautomator2 init
安装提示success即可
```

# uiautomator2服务
python -m uiautomator2 init
# 启动web页面查找元素命令
```
查看: http://atx.open.netease.com
启动: python -m weditor
安装方法: pip install --pre weditor
```

# 在安卓手机上运行自动化脚本
## 介绍 
1.QPython是一个能让安卓手机运行和编写Python的APP，Github下载地址下载链接
下载qpython-release.apk，然后使用adb install安装即可。

安装好之后，由于uiautomator2的库依赖huamanize、progress和requests，
打开QPython，点击QPYPI，然后点击INSTALL WITH PYTHON'S PYPI，分别执行:

```
pip install requests
pip install humanize
pip install progress
pip install --pre uiautomator2
```

2.将脚本文件push到手机内
```
adb push ~/Desktop/autou2/test_script.py /storage/emulated/0/qpython
adb push ~/Desktop/autou2/logger.py /storage/emulated/0/qpython
```

3.手机存储路径:/storage/emulated/0/qpython



# 在手机上运行脚本
1.打开QPython,点击执行脚本

2.脚本前置条件：微信需要登录 -> 在分享之前需要清除微信数据

3.脚本执行路径：

(1).启动app-点击随便看看-点击听书-点击主编力荐下的帖子-点击右上角分享-

(2) 击微信分享-吊起微信分享给指定的人-点击微信分享-点击留在微信-在微信列表页选择指定的人并点击-在会话详情页点击h5跳转链接并跳转.

(3)验证页面能正常打开/验证打开的页面的标题是之前分享的文章


# 定位方式

具体api文档参考:https://github.com/openatx/uiautomator2

## ResourceId定位
d(resourceId="com.smartisanos.clock:id/text_stopwatch").click()

## Text定位 
d(text="秒表").click()

## Description定位 
d(description="..").click()

## ClassName定位
d(className="android.widget.TextView").click()



# click
d(text="Settings").click()

# long click
d(text="Settings").long_click()

# 等待元素的出现
d(text="Settings").wait(timeout=10.0)

# adb屏幕录制
```
adb shell screenrecord /sdcard/demo.mp4

https://convertio.co/zh/mp4-gif/  mp4 to git
```

# 效果展示

效果在根目录下demo.mp4查看效果展示.

# 参考文档

### uiautomator官方文档,可以测试android原生app<br>
https://github.com/openatx/uiautomator2

### Android 手机内执行自动化<br>
https://testerhome.com/topics/11980

