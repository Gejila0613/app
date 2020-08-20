# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo4_qu_tiao_try import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('55555')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('123456')

driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()