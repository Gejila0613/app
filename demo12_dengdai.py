# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo5_denglu import driver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
#强制等待5秒
sleep(5)

#隐式等待
driver.implicitly_wait(20)

#显示等待
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver : WebDriver
# timeout : 最长超时时间，默认以秒为单位
# poll_frequency : 休眠时间的间隔时间，默认为0.5秒
# ignored_exceptions : 超时后的异常信息，默认情况下抛NoSuchElementException异常。

WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("elementID"))