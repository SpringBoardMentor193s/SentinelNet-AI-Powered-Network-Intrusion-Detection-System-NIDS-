import pandas as pd
import matplotlib.pyplot as plt


# NSL-KDD Dataset

#Load dataset
df = pd.read_csv("KDDTrain+.txt", header=None)

print("Number of rows:", len(df))
label_col = df.columns[-1]


print("Unique labels:", df[label_col].unique())

# Top 5 frequent attack types
print("Top 5 attack types:")
print(df[label_col].value_counts().head(5))

attack_counts = df[label_col].value_counts().head(10)

plt.figure(figsize=(10, 6))
attack_counts.plot(kind="bar")
plt.title("Top 10 Attack Types in NSL-KDD Dataset")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.show()

print(df.head())
print(df.info())
print(df.describe())

# CICIDS2017 Dataset

#Load dataset
cicids = pd.read_parquet("DoS-Wednesday-no-metadata.parquet")


print("CICIDS2017 Dataset Loaded")
print("Shape:", cicids.shape)

# Top 5 frequent attack types
if "Label" in cicids.columns:
    print("\nUnique attack types:", cicids["Label"].nunique())
    print("\nTop 5 frequent attack types:\n", cicids["Label"].value_counts().head())

    # Bar chart 
    cicids["Label"].value_counts().plot(kind="bar", figsize=(8,5))
    plt.title("CICIDS2017 Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")
    plt.show()


print(cicids.head())
print(cicids.info())
print(cicids.describe())
