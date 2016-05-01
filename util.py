# -*- coding:utf-8 -*-
import get
import string

def xml(page, url, filename):
    # 把饭否消息api输出的xml合并。
    end = '<?xml version="1.0" encoding="UTF-8"?>\n<statuses>\n</statuses>\n'
    while True:
        resp = get.get(page, url)
        if resp != end:
            #open函数里面的'a'是追加,改成'w'就是只写入会覆盖以前的内容.
            f=open(filename,'a')
            f.write(resp)
            # 每个write()后面必须close()才能写入.
            f.close()
        else:
            #把饭否api拉来的xml简单叠加到一起，然后进行下面的操作，重新读取文件然后把中间xml文件尾和头去掉。
            f = open(filename, 'r')
            result = f.read()
            f.close()
            result = string.replace(result, '\n</statuses>\n<?xml version="1.0" encoding="UTF-8"?>\n<statuses>\n', '\n')
            f=open(filename,'w')
            f.write(result)
            f.close()
            return True
        page = page + 1

def json(page, url, filename):
    # 把饭否消息api输出的json合并。
    end = '[]'
    while True:
        resp = get.get(page, url)
        if resp != end:
            #open函数里面的'a'是追加,改成'w'就是只写入会覆盖以前的内容.
            f=open(filename,'a')
            f.write(resp)
            # 每个write()后面必须close()才能写入.
            f.close()
        else:
            #处理json的方法简单粗暴，直接把饭否api拉来的数据叠加到一起，然后把中间json的尾头替换为逗号',' 一般文件应该不会影响性能。
            f=open(filename, 'r')
            result = f.read()
            f.close()
            result = string.replace(result, "]\n\n[", ",")
            f = open(filename, 'w')
            f.write(result)
            f.close()
            return True
        page = page + 1
