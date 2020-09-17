# -*- coding: utf-8 -*-


import logging
from  demo29_gonggong import gonggong
from demo27_qidongpeizhi import app_qidongpeizhi
from selenium.webdriver.common.by import By

class fzhdenglu(gonggong):

    yonghuming_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    mima_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    dengluanniu=(By.ID,'com.tal.kaoyan:id/login_login_btn')


    def denglu_kaishi(self,yonghuming,mima):
        self.jiancha_quxiao()
        self.jiancha_tiaoguo()

        logging.info('===============登录===============')
        logging.info('输入用户名:%s'%yonghuming)
        self.driver.find_element(*self.yonghuming_type).send_keys(yonghuming)

        logging.info('输入密码:%s'%mima)
        self.driver.find_element(*self.mima_type).send_keys(mima)

        logging.info('点击登录按钮.')
        self.driver.find_element(*self.dengluanniu).click()
        logging.info('登录完成 ')

if __name__ == '__main__':
    driver=app_qidongpeizhi()
    l=fzhdenglu(driver)
    l.denglu_kaishi('小可爱trr','trr123456')