# 📚 Amazon Books Analysis with Visualizations (Streamlit)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Amazon Books Analysis", layout="wide")
st.title("📚 Amazon Books Analysis with Visualizations")

# -----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv('datasets/bestsellers.csv')

# -----------------------------
# Data Overview
# -----------------------------
st.header("🔹 Dataset Overview")
st.write("First 5 rows of the dataset:")
st.dataframe(df.head())

st.write("Shape of dataset:", df.shape)
st.write("Columns:", df.columns.tolist())
st.write("Summary statistics:")
st.dataframe(df.describe())

# -----------------------------
# Data Cleaning & Processing
# -----------------------------
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

# -----------------------------
# Top Authors
# -----------------------------
st.header("📊 Top 10 Bestselling Authors")
author_counts = df['Author'].value_counts()
st.bar_chart(author_counts.head(10))

# -----------------------------
# Average Rating by Genre
# -----------------------------
st.header("📊 Average Rating by Genre")
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
st.bar_chart(avg_rating_by_genre)

# -----------------------------
# Price Distribution
# -----------------------------
st.header("📊 Price Distribution")
fig, ax = plt.subplots()
sns.histplot(df["Price"], bins=20, kde=True, color='coral', ax=ax)
ax.set_xlabel("Price ($)")
ax.set_ylabel("Count")
ax.set_title("Distribution of Book Prices")
st.pyplot(fig)

# -----------------------------
# Ratings Over Years
# -----------------------------
st.header("📊 Ratings Over Years")
fig2, ax2 = plt.subplots(figsize=(12,6))
sns.boxplot(x="Publication Year", y="Rating", data=df, palette="mako", ax=ax2)
ax2.set_title("Ratings Distribution Over Years")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
st.pyplot(fig2)

# -----------------------------
# Export results
# -----------------------------
st.header("💾 Exported CSVs")
author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
st.write("✅ CSV files saved: top_authors.csv, avg_rating_by_genre.csv")