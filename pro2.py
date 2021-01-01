import pandas as pd
df=pd.read_csv("data_csv.csv")
#NULL value found at code for Namibia
#replace code with 'NA' for Namibia
df=df.fillna("NA")
df=df.sort_values("Code")
dict=df.set_index("Code").T.to_dict('List')
for key,value in dict.items():
    dict[key]=value.pop()
countrycode1=input("Enter the first code")
countrycode2=input("Enter the second code")
for key,value in dict.items():
    if(key>countrycode1 and key<countrycode2):
        print(value)