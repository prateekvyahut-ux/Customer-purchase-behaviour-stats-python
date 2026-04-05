import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = sns.load_dataset("tips")
df.info()
df.head()
# Drop missing values
df.isnull().sum()
df = df.dropna()
df["total_bill"] = df["total_bill"].fillna(df["total_bill"].mean())

# === STEP 1: CENTRAL TENDENCY MEASURES ===
# Find mean of total_bill

print("Mean of total_bill:", df["total_bill"].mean())

# Find median of total_bill

print("Median of total_bill", df["total_bill"].median())

# Find mode of total_bill

print("Mode of Total_bill:", df["total_bill"].mode())

#Mean,Median and Mode for tip and size

print('Mean(tip)',df['tip'].mean())
print('median(tip)',df['tip'].median())
print('mode(tip)',df['tip'].mode())

print('Mean(size)',df['size'].mean())
print('Median(size)',df['size'].median())
print('Mode(size)',df['size'].mode())
#Central tendency across various group

gender_stats=df.groupby('sex')['total_bill'].agg(['mean','median'])
print(gender_stats)

day_wise=df.groupby('day')['total_bill'].agg(['mean','median'])
print(day_wise)

subgroup=df.groupby(['sex','day'])['total_bill'].agg(['mean','median'])
print(subgroup)

# === STEP 2: DISPERSION MEASURES ===
# Find range (max - min)

print("Range(total_bill)", (df["total_bill"].max() - df["total_bill"].min()))
print("Range(tips)", df["tip"].max() - df["tip"].min())

# Find variance

print("Variance(tips): ", df["tip"].var())
print("Varince(total_bill): ", df["total_bill"].var())

# Find standard deviation

print("standard deviation(total_bill): ", df["total_bill"].std())
print("standard deviation (tips)", df["tip"].std())

# Find IQR (Q3 - Q1)

Q3 = df["total_bill"].quantile(0.75)
Q1 = df["total_bill"].quantile(0.25)
q3 = df["tip"].quantile(0.75)
q1 = df["tip"].quantile(0.25)
print("IQR(total_bill)", Q3 - Q1)
print("IQR(tips)", q3 - q1)

# === STEP 3: VISUALIZATION ===
# Histogram of total_bill

plt.hist(df["total_bill"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()



# Boxplot of total_bill by sex

sns.boxplot(data=df, x="sex", y="total_bill")
plt.title("Boxplot of Total Bill by sex")
plt.xlabel("Sex")
plt.ylabel("Total Bill")
plt.show()


# Bar chart of transactions per day

sns.countplot(data=df, x="day",color='blue')
plt.title("Number of Transaction Per Day")
plt.xlabel("Day")
plt.ylabel("Number of Transaction")
plt.show()

# Scatter plot: size vs total_bill

sns.scatterplot(data=df, x="size", y="total_bill")
plt.title("Scatter Plot of Table Size Vs Total total_bill")
plt.xlabel("Table Size")
plt.ylabel("total_bill")
plt.show()


# === STEP 4: CORRELATION ===
# Compute Pearson correlation between size and total_bill

correlation = df["size"].corr(df["total_bill"])
print("Pearson Corelation between size and total_bill", correlation)

Corel=df['tip'].corr(df['total_bill'])
print("Pearson Correlation between tip and total_bill",Corel)
