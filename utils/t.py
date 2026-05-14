import pandas as pd

data = {
    "name": ["mukesh", "vikas", "rahul"],
    "role": ["QA", "developer", "manager"],
    "Experience": [5, 3, 8]
}

df=pd.DataFrame(data)
print(df)

df1=pd.read_csv("emp.csv")
print(df1)

df2=pd.read_excel("sample.xlsx")
print(df2)

print(df["Experience"].mean())