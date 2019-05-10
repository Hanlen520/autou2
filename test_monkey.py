#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
python uiautomator2 monkey自动化脚本
'''

import sys,time,unittest,logger,os
import uiautomator2 as u2
import random
reload(sys)
sys.setdefaultencoding('utf-8')
package_name = 'com.luojilab.player'
# app包名

Debug = True
event_wait = 0.3
count = 100


class monkey_test(unittest.TestCase):

    # 创建设备链接对象
    def driver(self):
        if Debug == True:
            devices_name = (os.popen("adb devices").readlines())[1].split()[0]
            # 手机设备号
            d = u2.connect_usb(devices_name)
        else:
            d = u2.connect('http://0.0.0.0:7912')
        return d


    def setUp(self):
        try:
            # app包名
            d = self.driver()
            d.app_start(package_name)
            d.implicitly_wait(5.0)
        except Exception as e:
            logger.logs("启动app失败:"+str(e))



    def test_run(self):
        '''
        :return:
        '''
        try:
            d = self.driver()
            logger.logs(u"app启动")
            window_size = d.window_size()
            point_x = window_size[0]
            point_y = window_size[1]
            global count
            while count > 0:
                x_random = random.randint( 0,point_x)
                y_random = random.randint( 0,point_y)
                print("点击坐标X:{},Y:{}".format(x_random,y_random))
                d.click(x_random, y_random)
                time.sleep(event_wait)
                count -= 1
        except Exception as e:
            logger.logs("测试用例执行异常:"+str(e))



    def tearDown(self):
        try:
            d = self.driver()
            d.app_stop(package_name)
        except Exception as e:
            logger.logs("关闭app异常:" + str(e))


if __name__ == '__main__':
    unittest.main()
