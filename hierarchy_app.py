import streamlit as st
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Hierarchical Clustering App")

# User input for data points
st.sidebar.header("Data Points Settings")
num_points = st.sidebar.slider("Number of Data Points", 10, 200, 50)

# Generate random data
data = np.random.rand(num_points, 2)

st.write("### Randomly Generated Data Points")
st.dataframe(data)

# Perform Hierarchical Clustering
linkage_method = st.sidebar.selectbox("Linkage Method", ["single", "complete", "average", "ward"])

if st.sidebar.button("Generate Dendrogram"):
    linked = linkage(data, method=linkage_method)

    # Plot dendrogram
    plt.figure(figsize=(10, 5))
    dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
    st.pyplot(plt)