 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Task 1: Load and Explore the Dataset ---
try:
    iris = load_iris(as_frame=True)  # Intentionally wrong for error handling test
    df = iris.frame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))
    print("First 5 rows:\n", df.head())
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    df = df.dropna()  # Drop missing values if any

    # --- Task 2: Basic Data Analysis ---
    print("\nBasic statistics:\n", df.describe())
    print("\nMean of numerical columns by species:\n", df.groupby('species').mean())

    # --- Task 3: Data Visualization ---
    sns.set(style="whitegrid")

    # 1. Line chart: Sepal length for first 30 samples
    plt.figure(figsize=(7,3))
    plt.plot(df.index[:30], df['sepal length (cm)'][:30], marker='o')
    plt.title('Sepal Length (First 30 Samples)')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: Average petal length per species
    plt.figure(figsize=(7,3))
    sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

    # 3. Histogram: Sepal width distribution
    plt.figure(figsize=(7,3))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: Sepal length vs. petal length by species
    plt.figure(figsize=(7,3))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Sepal Length vs. Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Error loading dataset:", e)


