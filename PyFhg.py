from openpyxl import workbook 
#引用工具包获取数据
import requests 
#引用工具包解析网页
from bs4 import BeautifulSoup  
#调用函数获取网页并保存到r
r=requests.get("http://piao.qunar.com/ticket/list.htm") 
#打印网页源代码
if r.status_code==200:  
    r.encoding = 'utf-8'    
#以格式重新编码网站
    html=r.text            
#解析网页
    soup = BeautifulSoup(html,"html.parser") 
    print(soup.prettify())
#赋循环初值
t=1    
#创建一个列表 保存第一次爬取数据
w=[]
#保存(txt)整理数据
w2=[]
#用while语句爬取六页数据
while t<6:
  r=requests.get("http://piao.qunar.com/ticket/list.htm?keyword=%E6%AD%A6%E6%B1%89&region=%E6%AD%A6%E6%B1%89&from=mpshouye_hotcity&page="+str(t))
#不能去掉 否则重复爬取六页
  if r.status_code==200:
    r.encoding = 'utf-8'
    html=r.text
    soup = BeautifulSoup(html,"html.parser")
  #print(soup.prettify())
  #不能去掉 否则重复爬取六页
  #创建四个列表
  a=[]#存取景点名称
  b=[]#存取地理位置
  c=[]#存取简介
  d=[]#存取月销量
  e=[]#存取价位
  
  
  #爬取景点名称
  for link in soup.find_all('a',class_="name"):   
      a.append(link.get_text())
  #爬取地理位置
  for link in soup.find_all('p',class_="address"):   
      b.append(link.get_text())
  #爬取简介
  for link in soup.find_all('div',class_="intro color999"):   
      c.append(link.get_text())

  #爬取月销量
  for link in soup.find_all('span',class_="hot_num"):   
      d.append(link.get_text())
  #爬取价位
  for link in soup.find_all('span',class_="sight_item_price"):   
      e.append(link.get_text())

  print("\n")
  i=0
  #打印并写入程序
  for i in range(len(a)):#代表从0到 len(a)
    print(a[i])
    print(b[i])
    print(c[i])
    print("月销量："+d[i])
    print("价位："+e[i][1:-2]+"元\n")
    #TypeError: append() takes exactly one argument (4 given) ,加[]
    w.append([a[i],b[i],c[i],int(d[i]),e[i]])
    
  t=t+1
#按照每行第四个数据月销量排序列表并保存到w1列表
w1=sorted(w,key = lambda s:s[3],reverse=True)



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
