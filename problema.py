import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("abc.xlsx")
#Linear plot between month and total profit 
xa=df["month_number"]
ya=df["total_profit"]
plt.plot(xa,ya)
plt.title("Profit Linear Plot")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()
