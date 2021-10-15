# coding=utf-8

import re

mm = "c:\\a\\b\\c"
print(mm)
ret = re.match("c:\\\\", mm).group()
print("c:\\\\-%s" % ret)

ret = re.match("c:\\\\a", mm).group()
print(ret)

# Python中字符串前面加上 r 表示原生字符串
ret = re.match(r"c:\\a", mm).group()
print(ret)
ret = re.match(r"c:\a", mm).group()
print(ret)
