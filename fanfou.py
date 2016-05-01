# -*- coding:utf-8 -*-
import sys
import string

#设置 $python2 fanfou.py 的默认值
try:
    parameter2 = sys.argv[2]
except IndexError:
    parameter2 = 'xml'
try:
    parameter1 = sys.argv[1]
except IndexError:
    parameter1 = 'backup'

# oauth检查设置
import get_token
get_token.oauth2()

import time
time = time.strftime("%Y-%m-%d %H:%M:%S")
filename = "backup"+time

if parameter1 == 'backup':
    baseUrl = 'http://api.fanfou.com/statuses/user_timeline'
    page=1
    import util
    #python没有switch语句，所以只能用if语句替代了。
    if parameter2 == 'xml':
        util.xml(page, url=baseUrl+'.xml', filename=filename+'.xml')
        print '备份文件backup'+time+'.xml成功!'
    elif parameter2 == 'json':
        util.json(page, url=baseUrl+'.json', filename=filename+'.json')
        print '备份文件backup'+time+'.json成功!'
    else:
        print '不知道备份成什么格式'
    


    

