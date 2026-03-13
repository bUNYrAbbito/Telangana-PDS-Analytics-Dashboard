import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


st.title("Telangana PDS Analytics Dashboard")
st.write("Fair Price Shop Performance Clustering and Anomaly Detection")


transactions = pd.read_csv("shop-wise-trans-details_5_2025.csv")
cards = pd.read_csv("fpshop-card-status_6_2025.csv")
shops = pd.read_csv("shop-status-details_6_2025.csv")


data = transactions.merge(cards, on="shopNo", how="left")
data = data.merge(shops, on="shopNo", how="left")


st.subheader("Dataset Preview")
st.write(data.head())


features = data[["latitude","longitude"]].dropna()


scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)


st.subheader("K-Means Clustering")

kmeans = KMeans(n_clusters=4, random_state=42)
features["cluster"] = kmeans.fit_predict(X_scaled)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=features["cluster"]
)

plt.title("KMeans Clusters")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")

st.pyplot(plt)


st.subheader("Shop Cluster Map")

m = folium.Map(location=[18.0,79.0], zoom_start=7)

for i,row in features.iterrows():

    folium.CircleMarker(
        location=[row["latitude"],row["longitude"]],
        radius=4,
        popup=f"Cluster {row['cluster']}",
        color="blue",
        fill=True
    ).add_to(m)


m.save("pds_shop_clusters.html")

st.success("Map exported successfully as HTML file")

folium_static(m)