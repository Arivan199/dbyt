import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_excel("abc.xlsx")
df.set_index("month_number")
x=[]
attributes=[]
for column in df:
    if(column != "month_number" and column !="total_units" and column !="total_profit"):
        x.append(df[column].sum())
        attributes.append(column)
newdf=df.append(pd.Series(x,index=attributes),ignore_index=True)
plt.title("Total sales of each product")
plt.pie(x,labels=attributes,autopct='%1.0f%%')
plt.show()