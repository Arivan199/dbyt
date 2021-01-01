#multiline plot between all products sale data and month number
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("abc.xlsx")
xa=df["month_number"]
pltb1=plt.plot(xa,df["facecream"],label="facecream")
pltb2=plt.plot(xa,df["facewash"],label="facewash",linewidth=4)
pltb3=plt.plot(xa,df["toothpaste"],label="toothpaste")
pltb4=plt.plot(xa,df["bathingsoap"],label="bathing soap")
pltb5=plt.plot(xa,df["shampoo"],label="shampoo")
pltb5=plt.plot(xa,df["moisturizer"],label="moisturizer",linewidth=2)
plt.title("Multiline Plot for each product")
plt.xlabel("month_number")
plt.ylabel("Product Sales")
plt.legend()
plt.show()