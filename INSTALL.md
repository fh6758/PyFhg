1.环境安装
1.安装Python3

2.安装其它组件，如Beautiful Soup 4(用于数据分析)。

a.安装requests库requests 库是一个简洁且简单的处理HTTP请求的第三方库。requests的最大优点是程序编写过程更接近正常URL 访问过程。
requests 库概述：这个库建立在Python 语言的urllib3 库基础上，类似这种在其他函数库之上再封装功能提供更友好函数的方式在Python 语言中十分常见。在Python 的生态圈里，任何人都有通过技术创新或体验创新发表意见和展示才华的机会。request 库支持非常丰富的链接访问功能，包括：国际域名和URL 获取、HTTP 长连接和连接缓存、HTTP 会话和Cookie 保持、浏览器使用风格的SSL 验证、基本的摘要认证、有效的键值对Cookie 记录、自动解压缩、自动内容解码、文件分块上传、HTTP(S)代理功能、连接超时处理、流数据下载等。
requests 库安装：采用pip3 指令安装  :\>pip install requests # 或者 pip3 install requests


b.安装beautifulsoup4 库 它是一个解析和处理HTML 和XML 的第三方库。
使用requests 库获取HTML 页面并将其转换成字符串后，需要进一步解析HTML页面格式，提取有用信息，这需要处理HTML 和XML 的函数库。beautifulsoup4 库，也称为Beautiful Soup 库或bs4 库，用于解析和处理HTML和XML。
注意：它不是BeautifulSoup 库。它的最大优点是能根据HTML 和XML 语法建立解析树，进而高效解析其中的内容。
优势： HTML 建立的Web 页面一般非常复杂，除了有用的内容信息外，还包括大量用于页面格式的元素，直接解析一个Web 网页需要深入了解HTML 语法，而且比较复杂。beautifulsoup4 库将专业的Web 页面格式解析部分封装成函数，提供了若干有用且便捷的处理函数。
实现：beautifulsoup4 库采用面向对象思想实现，简单说，它把每个页面当做一个对象，通过<a>.<b>的方式调用对象的属性（即包含的内容），或者通过<a>.<b>()的方式调用方法（即处理函数）。
引用：在使用beautifulsoup4 库之前，需要进行引用，由于这个库的名字非常特殊且采用面向对象方式组织，可以用from…import 方式从库中直接引用BeautifulSoup 类，方法如下。>>>from bs4 import BeautifulSoup

安装：采用pip 或pip3 指令安装beautifulsoup4 库，注意，不要安装beautifulsoup 库，后者由于年久失修，已经不再维护了:\>pip install beautifulsoup4 # 或者 pip3 install beautifulsoup4
2.获取网页内容

a.requests 库中的网页请求函数：get()是获取网页最常用的方式，在调用requests.get()函数后，返回的网页内容会保存为一个Response 对象，其中，get()函数的参数url 必须链接采用HTTP 或HTTPS方式访问。和浏览器的交互过程一样，requests.get()代表请求过程，它返回的Response 对象代表响应。返回内容作为一个对象更便于操作，Response 对象的属性如下表所示，需要采用<a>.<b>形式使用。

b.Response 对象的属性:status_code 属性返回请求HTTP 后的状态，在处理数据之前要先判断状态情况，如果请求未被响应，需要终止内容处理。
text 属性是请求的页面内容，以字符串形式展示
encoding 属性非常重要，它给出了返回页面内容的编码方式，可以通过对encoding 属性赋值更改编码方式，以便于处理中文字符
content 属性是页面内容的二进制形式
json()方法能够在HTTP 响应内容中解析存在的JSON 数据，这将带来解析HTTP的便利。
raise_for_status()方法能在非成功响应后产生异常，即只要返回的请求状态status_code 不是200，这个方法会产生一个异常，用于try…except 语句。使用异常处理语句可以避免设置一堆复杂的if 语句，只需要在收到响应调用这个方法，就可以避开状态字200 以外的各种意外情况。
requests 会产生几种常用异常。当遇到网络问题时，如：DNS 查询失败、拒绝连接等，requests 会抛出ConnectionError 异常；遇到无效HTTP 响应时，requests 则会抛出HTTPError 异常；若请求url 超时，则抛出Timeout 异常；若请求超过了设定的最大重定向次数，则会抛出一个TooManyRedirects 异常。




  


c.获取一个网页内容







d.查找对应标签


当需要列出标签对应的所有内容或者需要找到非第一个标签时，需要用到BeautifulSoup 的find()和find_all()方法。这两个方法会遍历整个HTML 文档，按照条件返回标签内容。
BeautifulSoup 的find_all()方法可以根据标签名字、标签属性和内容检索并返回标签列表，通过片段字符串检索时需要使用正则表达式re 函数库，re 是Python 标准库，直接通过import re 即可使用。
采用re.compile('jquery')实现对片段字符串（如'jquery'）的检索。当对标签属性检索时，属性和对应的值采用JSON格式，例如：'src':re.compile('jquery')其中，键值对中值的部分可以是字符串或者正则表达式。
除了find_all()方法，BeautifulSoup 类还提供一个find()方法，它们的区别只是前者返回全部结果而后者返回找到的第一个结果，find_all()函数由于可能返回更多结果，所以采用列表形式；find()函数返回字符串形式。







3.分析网页内容并提取有用数据到恰当的数据结构中

①#导入txt
#导入txt已排序的数据
i=0 #赋初值
for i in range(len(w1)):   #代表从0到 len(w1)
  w2.append("\n景点："+w1[i][0]+"\n"+w1[i][1]+"\n简介："+w1[i][2]+"\n月销量："+str(w1[i][3])+"\n价位："+w1[i][4][1:-2]+"元\n")

#print(w2)  #测试已排序好的列表是否正确
#覆盖写入,打开文件，注意路径前的"r"不可省略，a尾部追加写入
f=open(r'景点.txt', 'w',encoding='utf-8')
i=0 #赋初值
for i in w2:    #逐行把列表w2的数据写入txt中
    f.writelines(i) #写入按销售量排序的列表,f.write\f.writelines都可以
    f.writelines("\n") #写入并换行
f.close()#关闭文件



②#写入excel中
#导入excel已排序的数据
#创建Excel表并写入数据
wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
# 往表中写入标题行,以列表形式写入！
ws.append(['景点', '地址', '简介', '月销量', '价位'])
i=0  #赋初值
for i in range(len(w1)):
        # 所有数据按行写入工作表中
        ws.append([w1[i][0], w1[i][1][3:], w1[i][2], w1[i][3],w1[i][4][1:-2]])
#存入所有信息后，保存为tourism.xls
wb.save('tourism.xls') 