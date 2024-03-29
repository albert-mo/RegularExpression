# coding=utf-8

import re

# 需求：匹配出文章阅读的次数

ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())  #9999

# 需求：统计出python、c、c++相应文章阅读的次数

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)  # ['9999', '7890', '12345']

# sub
# 需求：将匹配到的阅读次数加1

# 方法一
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)


# 方法二
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)

# 从下面的字符串中取出文本
test_str = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
"""
# ^	匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。
res = re.sub(r"<[^>]*>|&nbsp;|\n", "", test_str)
print(res.group)
res_sub = re.sub(r"<[^>]*>", "", test_str)
print(res_sub)

# split 根据匹配进行切割字符串，并返回一个列表
# 按照:或者空格分割
ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
print(ret)