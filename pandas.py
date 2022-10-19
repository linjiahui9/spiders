from pandas import read_excel
from pandas import DataFrame
import pandas as pd
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
df[-3:][["大学英语I"，"大学英语II","大学英语III","大学英语IV"]]
df[-3:]["大学英语I":"大学英语IV"]
df[-3:].loc[:,"大学英语I":"大学英语IV"]
df.loc[df.index[-3]:df,index[-1],"大学英语I":"大学英语IV"]
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
df.drop('备注'，axis=1)    # 设置删除轴向为1表示列
# 修改数据的列标题为：标题1，标题2...
df.columns['标题1','标题2']
# 为数据添加一列备注
# 为数据增加新的一行记录
