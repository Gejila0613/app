# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com


from demo4_qu_tiao_try import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

root_element=driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()