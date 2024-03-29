# coding=utf-8

import re

# 示例1：|
# 需求：匹配出0-100之间的数字

ret = re.match("[1-9]?\\d", "8")
print(ret.group())  # 8

ret = re.match("[1-9]?\\d", "78")
print(ret.group())  # 78

# 不正确的情况
ret = re.match("[1-9]?\\d", "08")
print(ret.group())  # 0

# 修正之后的
ret = re.match("[1-9]?\d$", "08")
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

# 添加|
ret = re.match("[1-9]?\\d$|100", "8")
print(ret.group())  # 8

ret = re.match("[1-9]?\\d$|100", "78")
print(ret.group())  # 78

ret = re.match("[1-9]?\\d$|100", "08")
# print(ret.group())  # 不是0-100之间

ret = re.match("[1-9]?\\d$|100", "100")
print(ret.group())  # 100

print('*'*50)

# 需求：匹配出163、126、qq邮箱

ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())  # test@qq.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱

print('*'*50)

# 1开头，不是以4、7结尾的手机号码(11位)

tels = ["13100001234", "18912344321", "10086", "18800007777", "08912344321"]

for tel in tels:
    ret = re.match("1\\d{9}[0-35-68-9]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)

print('*'*50)

# 示例2：( )
# 提取区号和电话号码

ret = re.match("([^-]*)-(\\d+)", "010-12345678")
if ret:
    print("区号：%s" % ret.group(1))
    print("电话号码：%s" % ret.group(2))
else:
    print("格式错误1")

print('*'*50)

# 示例3：\
# 需求：匹配出<html>hh</html>

# 能够完成对正确的字符串的匹配
ret = re.match("<[a-zA-Z]*>\\w*</[a-zA-Z]*>", "<html>hh</html>")
print(ret.group()) # <html>hh</html>

# 如果遇到非正常的html格式字符串，匹配出错
ret = re.match("<[a-zA-Z]*>\\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
print(ret.group())

# 正确的理解思路：如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么

# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())

# 因为2对<>中的数据不一致，所以没有匹配出来
test_label = "<html>hh</htmlbalabala>"
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", test_label)
if ret:
    print(ret.group())
else:
    print("%s 这是一对不正确的标签" % test_label)

print('*'*50)

# 示例4：\number
# 需求：匹配出<html><h1>www.itcast.cn</h1></html>

labels = ["<html><h1>www.itcast.cn</h1></html>",
          "<html><h1>www.itcast.cn</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

print('*'*50)

# 示例5：(?P<name>) (?P=name)
# 需求：匹配出<html><h1>www.itcast.cn</h1></html>

labels = ["<html><h1>www.itcast.cn</h1></html>",
          "<html><h1>www.itcast.cn</h2></html>"]

for label in labels:
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)