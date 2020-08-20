# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo4_qu_tiao_try import driver
from time import sleep

#获取屏幕尺寸
def chicun():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

l=chicun()
print(l)

def xiangzuo():
    l = chicun()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

for i in range(2):
    xiangzuo()
    sleep(0.5)



