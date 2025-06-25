import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data={
    "StudyHours" : [1, 2, 2.5, 3, 4, 8, 7.5 ,8.5, 9, 7, 5],
    "SleepHours" : [9, 8.5, 8, 7.5, 7, 5, 4.5, 4, 3.5, 5.5, 6]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3 , random_state=42)
kmeans.fit(df)

df['Cluster'] = kmeans.predict(df)

sorted_indices= np.argsort(kmeans.cluster_centers_[:,0])

lable_map={
    sorted_indices[0]: "Low study",
    sorted_indices[1]: "Balanced",
    sorted_indices[2]: "High study"
}

df['ClusterLable'] = df['Cluster'].map(lable_map)

plt.figure(figsize=(8, 6))
plt.scatter(df['StudyHours'], df['SleepHours'], c=df['Cluster'], cmap='Accent', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, color='red', label='Center')
plt.xlabel("StudyHours")
plt.ylabel("SleepHours")
plt.title("K-means")
plt.legend()
plt.grid(True)
plt.show()

print(df[['StudyHours' , 'SleepHours' , 'ClusterLable']])