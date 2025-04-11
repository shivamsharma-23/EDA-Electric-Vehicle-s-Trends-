#PYTHON PROJECT

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# LOADING DATA AND REPLACING NULL VALUES 
data = pd.read_csv("C:\\Users\\shiva\\Downloads\\Electric_Vehicle_Population_Data (1).csv")
data.replace("*", pd.NA, inplace=True)
data.replace(".", pd.NA, inplace=True)
data.to_csv("Cleaned_EV_File.csv", index=False)

#CHECKING STRUCTURE
data.info()
data.describe()
print(data.isnull().sum())

#LOADING CLEAN DATA(JOH BAAD M AAYA HAI)
df = pd.read_csv("Cleaned_EV_File.csv")

# Fill missing values in key numeric columns
df['Electric Range'].fillna(df['Electric Range'].mean(), inplace=True)
df['Base MSRP'].fillna(df['Base MSRP'].mean(), inplace=True)

# Create new columns
df['Average_Expenditure'] = df['Base MSRP']
df['Performance_Category'] = np.where(df['Base MSRP'] > df['Base MSRP'].mean(), 'High', 'Low')

# Top 10 Counties by Avg Expenditure
top10 = df.groupby('County')['Base MSRP'].mean().sort_values(ascending=False).head(10).reset_index()
print("Top 10 Counties with Highest Average MSRP:\n")
print(top10)

# State-wise EV count
statewise = df['State'].value_counts().head(10)
print("Top 10 States by EV Count:\n")
print(statewise)

# Performance summary
performance = df.groupby('Performance_Category')['Electric Range'].mean()
print("Performance Category Based on MSRP:\n")
print(performance)

# 1. Top 10 Most Registered EV Models
top_models = df['Model'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_models.values, y=top_models.index, palette='cubehelix')
plt.title("Top 10 Most Registered EV Models")
plt.xlabel("Number of Registrations")
plt.ylabel("Model")
plt.show()


# 2. Distribution of Electric Range
plt.figure(figsize=(10,5))
sns.histplot(df['Electric Range'], bins=30, kde=True, color='mediumseagreen')
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Frequency")
plt.show()

# 3. Average MSRP by Make
avg_msrp = df.groupby('Make')['Base MSRP'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=avg_msrp.values, y=avg_msrp.index, palette='magma')
plt.title("Top 10 EV Makes by Average MSRP")
plt.xlabel("Average MSRP ($)")
plt.ylabel("Make")
plt.show()

# 4. EV Count Over Model Year
plt.figure(figsize=(12,5))
sns.countplot(x='Model Year', data=df, palette='viridis', order=sorted(df['Model Year'].unique()))
plt.title("Number of EVs by Model Year")
plt.xlabel("Model Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 5. Electric Range vs MSRP
plt.figure(figsize=(10,6))
sns.scatterplot(x='Electric Range', y='Base MSRP', hue='Electric Vehicle Type', data=df)
plt.title("Electric Range vs MSRP")
plt.xlabel("Electric Range (miles)")
plt.ylabel("MSRP ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 6. Correlation  Ka Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 7. Boxplot of MSRP by Vehicle Type
plt.figure(figsize=(10,6))
sns.boxplot(x='Electric Vehicle Type', y='Base MSRP', data=df, palette='Pastel1')
plt.title("MSRP Distribution by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("MSRP ($)")
plt.xticks(rotation=45)
plt.show()

# 8. Pairplot of Key Numeric Features (Updated with Hue by Vehicle Type)
selected = df[['Electric Range', 'Base MSRP', 'Model Year', 'Electric Vehicle Type']]
sns.pairplot(selected, hue='Electric Vehicle Type', palette='coolwarm')
plt.suptitle("Pairwise Relationships of Key Features by Vehicle Type", y=1.02)
plt.show()


# 9. Pie Chart of Vehicle Types
vehicle_type_counts = df['Electric Vehicle Type'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(vehicle_type_counts, labels=vehicle_type_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set3'))
plt.title("EV Type Distribution")
plt.show()




df.to_csv("Modifiead_Project_File.csv")

































