# coding=utf-8

import re

# Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；
# 非贪婪则相反，总是尝试匹配尽可能少的字符。
# 在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
s = "This is a number 234-235-22-423"
# 不加?,贪婪匹配，.+尽可能多的匹配字符
r = re.match(".+(\d+-\d+-\d+-\d+)", s)
print(r.group(1))  #4-235-22-423
# 加?,非贪婪匹配,.+匹配尽可能少的字符
r = re.match(".+?(\d+-\d+-\d+-\d+)", s)
print(r.group(1))  #234-235-22-423

test_str = '''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
'''
res = re.search(r"https://.*?\.jpg", test_str)
print(res.group())