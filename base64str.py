#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这是一个base64编解码的小demo
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#
import base64

aim = raw_input("what's your chose \n1:encode \n2:decode \n0:exit \n")
aim = int(aim)
while aim > 0:
    if aim == 1:
        str = raw_input('please input your string:(encode)\n')
        str = str.encode("utf8")
        print "the encode str is:"
        result = base64.b64encode(str)
        print result
    elif aim == 2:
        str = raw_input('please input your string:(decode)\n')
        str = str.encode("utf8")
        print "the decode str is:"
        result = base64.b64decode(str)
        print result
    else:
        print aim
    aim = raw_input("what's your chose \n1:encode \n2:decode \n0:exit \n")
    aim = int(aim)

