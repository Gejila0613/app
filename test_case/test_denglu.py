# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo31_unit import kaishijieshu
from demo30_fzhdenglu import fzhdenglu
import unittest
import logging

class Testdenglu(kaishijieshu):

    def test_denglu_cm01(self):
        logging.info('=========开始登录cemaxueyuan01============')
        l= fzhdenglu(self.driver)
        l.denglu_kaishi('cemaxueyuan01','cema123456')


    def test_denglu_cm02(self):
        logging.info('==========开始登录cemaxueyuan02========')
        l=fzhdenglu(self.driver)
        l.denglu_kaishi('cemaxueyuan02','cema123456')


    def test_login_error(self):
        logging.info('=======test_login_error=========')
        l=fzhdenglu(self.driver)
        l.denglu_kaishi('666','222')


if __name__ == '__main__':
    unittest.main()
