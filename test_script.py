#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
python uiautomator2自动化测试脚本
'''

import sys,time,unittest,logger,os
import uiautomator2 as u2
reload(sys)
sys.setdefaultencoding('utf-8')

package_name = 'com.luojilab.player'
# app包名

share_name = u"xxxxx"
# 分享给谁

Debug = False


class android_test(unittest.TestCase):

    # 创建设备链接对象
    def driver(self):
        if Debug == True:
            devices_name = (os.popen("adb devices").readlines())[1].split()[0]
            # 手机设备号
            d = u2.connect_usb(devices_name)
        else:
            d = u2.connect('http://0.0.0.0:7912')
        return d

    # 启动app
    def setUp(self):
        try:
            # app包名
            d = self.driver()
            d.app_start(package_name)
            time.sleep(3)

        except Exception as e:
            logger.logs("启动app失败:"+str(e))

    # 清除微信app数据
    def clear_wechat(self):
        pass


    def login_wechat(self):
        d = self.driver()
        # 操作微信客户端
        d(resourceId="com.tencent.mm:id/ht").set_text("xxxxxxx")
        d(resourceId="com.tencent.mm:id/ht", text=u"••••••••").set_text("••••••••")
        d(resourceId="com.tencent.mm:id/byd").click()
        time.sleep(10)

    # 测试case
    def testcase(self):
        try:
            d = self.driver()
            logger.logs(u"app启动")

            # # 判断登录状态
            # if d(text=u"随便看看").info['text']:
            #     d(text=u"随便看看").click()

            # 点击听书
            d(text=u"听书").click()

            logger.logs(u"点击听书")

            # 获取主编力荐的列表页的文案
            get_text = d(resourceId="com.luojilab.player:id/tv_product_name").info['text']

            logger.logs(get_text)

            # 点击主编力荐
            d(resourceId="com.luojilab.player:id/tv_product_name").click()

            # 点击分享
            d(resourceId="com.luojilab.player:id/shareButton").click()
            d(text=u"微信").click()

            # 点击分享给share_name
            d(text=share_name, className="android.widget.TextView").click()

            # 点击微信中分享按钮
            d(text=u"分享", className="android.widget.Button").click()

            # 点击留在微信
            d(text=u"留在微信").click()

            # 点击微信列表中share_name
            d(text=share_name, className="android.view.View").click()

            # 点击微信会话中的分享h5链接
            d(text=get_text, className="android.widget.TextView").click()

            # 获取h5页面中title的文案
            title = d(resourceId="android:id/text1").info['text']

            logger.logs("获取title:"+str(title))

            # 判断title和之前获取的文案是否相同
            if get_text in title:
                self.assertTrue(True)
                logger.logs("微信h5页面验证分享成功")

            else:
                self.assertFalse(True)
                logger.logs("微信h5页面验证分享失败")

        except Exception as e:
            logger.logs("测试用例执行异常:"+str(e))

    # 关闭app
    def tearDown(self):
        try:
            d = self.driver()
            d.app_stop(package_name)
        except Exception as e:
            logger.logs("关闭app异常:"+str(e))


if __name__ == '__main__':
    unittest.main()
