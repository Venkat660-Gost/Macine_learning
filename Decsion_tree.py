import pandas as pd
from sklearn.tree import DecisionTreeClassifier
df=pd.read_excel("Student_grade.xlsx")
df.columns=df.columns.str.strip()
print("Columns",df.columns.tolist)
X=df[['Hours','Attendance']]
y=df['Result']
model=DecisionTreeClassifier()
model.fit(X,y)
hours=int(input("Enter no of hours:"))
attendance=int(input("Enter Attandence:"))
new_data=pd.DataFrame({
    "Hours":[hours],
    "Attendance":[attendance]
})
pre=model.predict(new_data)
print(pre[0])




