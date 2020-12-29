# coding=utf-8

import re

# 匹配任意1个字符（除了\n）
ret = re.match(".", "M")
print(ret.group())

ret = re.match("t.o", "too")
print(ret.group())

ret = re.match("t.o", "two")
print(ret.group())

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到3,5-9
ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
# print(ret.group())
try:
    print(ret.group())
except AttributeError:
    print("未匹配到数据")

# 普通的匹配方式
ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥2号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥3号", "嫦娥3号发射成功")
print(ret.group())

# 使用\d进行匹配
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
print(ret.group())

# 匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

