# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo4_qu_tiao_try import driver
import random

#进入注册界面选择并设置头像
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[2].click()

driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#注册信息填写（如果有短信验证码或者图形验证码，如果公司内部测试，就让开发给你一个万能码或者把这个注释掉）
username='trr2020'+'FLY'+str(random.randint(1000,9000))
print('username: %s' %username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

password='trr'+str(random.randint(10000,90000))
print('password: %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email='trr'+str(random.randint(1000,9000))+'@163.com'
print('email: %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()


#院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
#选择省份
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
#选择具体院校--同济大学
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()


#专业选择

driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
#选择经济学类-统计学-经济统计学
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()


#点击“进入考研帮”按钮

driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()