#!/usr/bin/env python
# coding: utf-8

# In[241]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import requests
import pandas as pd
import numpy as np
import csv
from io import StringIO
#先處理指數
bigdata = []
index = []
time = []
# 載股價
r = requests.post('https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=csv&date=20210101')
df = csv.reader(StringIO(r.text.replace("=", "")))
bigdata += df

#處理農曆日期
for i in range(2,len(bigdata)):
    index.append(float(bigdata[i][4].replace(',','')))
    time.append(i-1)
    
from zhdate import ZhDate
from datetime import datetime
for i in range(2,len(bigdata)):
    print(i-1,str(ZhDate.from_datetime(datetime(int(bigdata[i][0].split('/')[0])+1912,int(bigdata[i][0].split('/')[1]),int(bigdata[i][0].split('/')[2])))))
#畫圖
print('8-22買','1-7 or 23-30賣')
fig = plt.figure(figsize=(15,4))    # 设置画布大小
plt.plot(time , index ,'g')


# In[ ]:





# In[242]:


market = 0
cash = 50000


# In[ ]:





# In[243]:


#漲跌
for i in range(2,len(bigdata)):
    if i == 2:
        print(k)
        print(i-1,cash,market)
        continue
    else:
        flow = ((float(bigdata[i][4].replace(',',''))-float(bigdata[i-1][4].replace(',','')))/float(bigdata[i][4].replace(',','')))+1
        market = market*flow
        k = str(ZhDate.from_datetime(datetime(int(bigdata[i][0].split('/')[0])+1912,int(bigdata[i][0].split('/')[1]),int(bigdata[i][0].split('/')[2]))))[-3:]
        if k == '13日' or k =='14日' or k=='15日' or k == '16日' or k== '17日':
            market += cash
            cash -= cash
            print(i-1,cash,market,sell)
        elif k == '月1日' or k == '月2日' or k == '月3日' :
            cash += market
            market -= market
            print(i-1,cash,market,sell)
        else :
            print(i-1,cash,market,sell)
print(cash+market)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




