import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
df=pd.read_excel("emails.xlsx")
vector=TfidfVectorizer()
X=vector.fit_transform(df["Email"])
#Label
y=df["Label"]
model=MultinomialNB()
model.fit(X,y)
#User email
email=input("Enter Email:")
#Convert inputr email
email_vector=vector.transform([email])
#predict
predict=model.predict(email_vector)

print(predict[0])