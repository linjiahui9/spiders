from pandas import read_excel
from pandas import DataFrame
import pandas as pd

'''
pd.set_option('display.max_columns',10)
df=read_excel('C:/Users/Administrator/Desktop/09电动1.xls')

# 输出前三条记录
df.head(3)	
df[0:3]
# 输出最后三条记录
df[-3:]
df.tail(3)
# 输出最后三条记录的前三列
df.iloc[-3:, 0:3]
# 输出最后三条记录的所有大学英语成绩
df[-3:][["大学英语I","大学英语II","大学英语III","大学英语IV"]]
df[-3:]["大学英语I":"大学英语IV"]
df[-3:].loc[:,"大学英语I":"大学英语IV"]
df.loc[df.index[-3]:df.index[-1],"大学英语I":"大学英语IV"]
# 输出第一条记录（从1开始算）的C语言程序设计成绩
df.at[0,'C语言程序设计']
df.iat[0,8]
# 输出所有没有选修肚皮舞的记录
df[df['肚皮舞'].isnull()]
df[df.肚皮舞.isnull()]
df[df.肚皮舞.isna()]
# 输出C语言程序设计在90分以上的记录
df['C语言程序设计']>=90
df[df['C语言程序设计']>=90]   # 筛选记录所在的行
# 获取“吴海游”的C语言程序设计和电路成绩
df[df['姓名'] == '吴海游'][['C语言程序设计','电路']]     # 先找行再找列
df[['C语言程序设计','电路']][df['姓名'] == '吴海游']
# 为数据设置索引：1-36
df.index=range(1,37)
# 为数据添加一列备注
df['备注']= ''
# 删除数据中的test列
df.drop('备注',axis=1)    # 设置删除轴向为1表示列
# 修改数据的列标题为：标题1，标题2...
df.columns['标题1','标题2']
# 为数据添加一列备注
# 为数据增加新的一行记录

'''

pd.set_option('display.max_columns',8)
df = read_excel(r'D:data\rz2.xlsx')

newDF = df.drop_duplicates()
newDF = df.dropna()
df.fillna(0)

df,fillna(method = 'bfill')     # 后一个值填充缺失值

df.IP.str.strip()
df.IP.str.strip().str.slice(0,3)
df.IP.str.strip('.')
df.IP.str.strip('.', n = 2)
df.IP.str.strip('.', n = 2, expand = True)

df[df.TCSJ.str.contains('189', na = False)]
df[df.TCSJ.astype(str).str.contains('189', na = False)]
df[df.TCSJ.astype(str).str.contains('189', na = True)]

import numpy as np
df.loc[len(df)] = ['aa', np.nan, np.nan, np.nan, np,nan]
df[df.IP.str.contains('222', na = False)]
df[df.IP.str.contains('222', na = True)]

fromn pandas import Series
ss = Series([6,5,7,4])

from pandas import DataFrame
df0={'Ohio':[0,6,3],'Texas':[7,4,1],'California':[2,8,5]}
df=DataFrame(df0.index=['a','c','d'])

ser = Series([4.5,7.2,-5.3,3.6].index = ['a','b','c','d'])

A = ['a','b','c','d','e']
ser.reindex(A)

A = ['d','b','c','e','a']
ser.reindex(A,fill_value=0)

ser = Series([4.5,7.2,-5.3,3.6],index = ['a','b','c','d'])
A = ['d','b','c','e','a']
ser.reindex(A, method='ffill')

A = ['d','b','c','e','a']
ser.reindex(A, method = 'bfill')

A = ['d','b','c','e','a']
ser.reindex(A, method = 'bfill',fill_value = 0)








