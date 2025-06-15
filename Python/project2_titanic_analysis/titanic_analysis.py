# titanic_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
print("📦 Loading Titanic dataset...")
df = pd.read_csv("train.csv")

# Basic info
print("\n🔍 Dataset shape:", df.shape)
print(df.head())

# Show missing values
print("\n❓ Missing values:\n", df.isnull().sum())

# Handle missing data
df.loc[:, "Age"] = df["Age"].fillna(df["Age"].median())
df = df.drop(columns=["Cabin"])  # Drop column with too many nulls
df = df.dropna(subset=["Embarked"])  # Drop rows where Embarked is null

# Plot 1: Survival by Gender
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()

# Plot 2: Survival by Passenger Class
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()

# Plot 3: Age Distribution
sns.histplot(df["Age"], kde=True, bins=30)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 4: Correlation Heatmap
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()
