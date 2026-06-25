from sklearn.cluster import KMeans
import pandas as pd
df=pd.read_excel("House_data.xlsx+.xlsx")
X=df[["Area","Bedrooms"]]
kmeans=KMeans(n_clusters=2,random_state=42)
#Train model
kmeans.fit(X)
#Assian clusters
df["Cluster"]=kmeans.labels_
print(df)
#save result
df.to_excel("clustered_House_data.xlsx+.xlsx",index=False)