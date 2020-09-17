# -*- coding: utf-8 -*-


from demo4_qu_tiao_try import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('小可爱trr')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('654321')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


error_message="用户名或密码错误，你还可以尝试4次"
limit_message="验证失败次数过多，请15分钟后再试"
#\'转义，{}用到了一个format格式化把内容放到里面
message='//*[@text=\'{}\']'.format(error_message)
# message='//*[@text=\'{}\']'.format(limit_message)
#显示等待lambda匿名函数，如果获取不到会超时报错
toast_element=WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)