# coding=utf-8
import re

# 匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

# 匹配出，变量名是否有效
names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    # \w  匹配单词字符，即a - z、A - Z、0 - 9、_
    ret = re.match("[a-zA-Z_]+[\w]*", name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)

# 匹配出，0到99之间的数字
ret = re.match("[1-9]?[0-9]", "7")
print(ret.group())

ret = re.match("[1-9]?\d", "33")
print(ret.group())

ret = re.match("[1-9]?\d", "09")
print(ret.group())

# 匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())
