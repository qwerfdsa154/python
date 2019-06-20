#!/usr/bin/env python
# coding: utf-8

# # 加法

# In[ ]:


a=3
b=5
a+b


# # 網頁擷取

# In[1]:


import requests
a=requests.get("http://www.must.edu.tw/")
print(a.text)


# # 單行註解

# In[2]:


#單行註解


# # 多行註解

# In[ ]:


'''
多行註解
'''


# # 設定變數

# In[ ]:


x=5


# # 印出變數

# In[3]:


x,y,z = 7,8,9
print(x)
print(y)
print(z)


# # 一般的加法、乘法、次方

# In[4]:


x,y,z = 3,6,9
x += 1      
y *= 5      
z **=6      
print(x,y,z)


# # 傳回輸入數值的平方根

# In[5]:


import math
a,b,c=3,4,5
s=(a+b+c)/2
d=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(d)


# # 傳回值

# In[6]:


x=254
print(type(x))
id(x)


# # 求圓錐體面積

# In[7]:


#半徑為4.5，el 高度為4.5的圓錐體面積為何?
import math
print((4.5*4.5*math.pi*4.5)/3)


# # 除法以及求商跟餘數

# In[8]:


x=16
y=3
print(x/y)
print(x//y) 
print(x%y) 


# # 關係運算

# In[9]:


x=10
print(20==20)
y=20
print(x==y)
x=y
print(x)


# # 判斷是否為真

# In[10]:


a,b,c=10,20,30
print(a<=b<=c)


# # 減法

# In[11]:


x=3.141592627
print(x-3.14)


# # 判斷是否為真

# In[ ]:


y=2010
print(y%4==0 and y%100!=0 or y%400==0)
y=2012
print(y%4==0 and y%100!=0 or y%400==0)
y=2000
print(y%4==0 and y%100!=0 or y%400==0)


# # 型態轉換

# In[12]:


x=12
y=float(x)+0.5
print(y)
print(int('123'))
print(float('123'))
print(int(123.333))
x=10*3.25              #3.25
y=200*200              #40000
s='The value of x is ' + str(x) + 'and y is ' + str(y)
s1='The value of x is ' + repr(x) + 'and y is ' + repr(y)
print(s)
print(s1)


# # 圓周率、求2的3次方、平方根

# In[2]:


import math
print(math.pi)
print(math.pow(2,3))
print(8.3*10.58*math.sin(37.0/180*math.pi)/2)
print(math.sqrt(25))


# # 輸入半徑後求圓面積

# In[ ]:


import math
r= input("請輸入半徑:")
area = float(r) * float(r) *math.pi
print("圓面積為:" ,area)


# # List串列

# In[3]:


my_list0 = [1,2,3]
print(my_list0)
my_list1 = ['python' ,'js','SQL']
print(my_list1[0])
my_list1.append('java')
print(my_list1)


# # 新增到特殊位置

# In[4]:


my_list1.insert(0,'c#')
print(my_list1)
print(len(my_list1))


# # list長度

# In[5]:


my_list2=['c#','python' ,'js','SQL','java']
print(len(my_list2))
print(len(my_list2[1]))


# # 刪除某特定物件、某特定位置的物件、-1指的是從最後數來第一個位置

# In[6]:


my_list3=['c#','python' ,'js','SQL','java']
my_list3.remove('js')    #刪除某特定物件
print(my_list3)
del my_list3[0]          #刪除某特定位置的物件
print(my_list3)
del my_list3[-1]         #-1指的是從最後數來第一個位置
print(my_list3)


# # 檢查是否存在

# In[7]:


print('java' in['python' ,'js','SQL'])


# # 串列反轉跟串列排序

# In[9]:


a=[1,2,3,4,5,6,7,8,9]
print(a)
a.reverse()   
print(a)
a.sort()    
print(a)


# # 取特定位置的值

# In[10]:


a=[123,'abc',[111,222],[333,444]]
print(a[0])
print(a[1])
print(a[2])
print(a[2][1])


# # 不同的字串相加

# In[11]:


a=[111,222] + [333,444] + [4156,1546]
print(a)


# # 串列List常用在For迴圈

# In[12]:


shoplist = ['milk','egg','coffee','banana']
for item in shoplist:
    print(item)


# # tupe的元素不可新增刪除或修改

# In[13]:


a_list=['python' ,'js','SQL']
a_tuple=('python' ,'js','SQL')
b_tuple=tuple(a_list)
print(type(a_list))
print(type(a_tuple))
print(b_tuple)


# # 判斷類型

# In[14]:


c_tuple= 111,333,222   #c_tuple=(111,2222,333)
print(c_tuple)
print(type(c_tuple))


# # dict(字典-dictiontry)
# 
# # 帶有鍵值(key)的list

# In[ ]:


a_list=['python', 'js', 'c#']
a_dict={0:'python', 1:'js', 2:'c#'}
print(a_list[0])
print(a_dict[0])
b_dict={'1st':'python', '2nd':'js','3rd':'c#'}
print(b_dict['1st'])

