#linear regrassion
from sklearn.linear_model import LinearRegression #libreary
import pandas as pd                          #libreary for importring excal data
df=pd.read_excel("House_data.xlsx+.xlsx")
print(df)
X=df[["Area","Bedrooms"]]
y=df["Price"]
model=LinearRegression()
model.fit(X,y)
Area=int(input("Enter the area:"))
Bedrooms=int(input("Enter the beds:"))
new_data=pd.DataFrame({
    "Area":[Area],
    "Bedrooms":[Bedrooms]
})
pre=model.predict(new_data)
print(pre)
