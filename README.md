# Project Explanation
This project demonstrates basic data analysis and visualization using the classic Iris dataset. The workflow is divided into three main tasks:

# 1. Load and Explore the Dataset
Loading: The Iris dataset is loaded using sklearn.datasets.load_iris with the as_frame=True option to get a pandas DataFrame.
Inspection: The first five rows of the dataset are displayed to give an overview of the data.
Structure: The code prints the data types of each column and checks for missing values.
Cleaning: Any missing values are dropped to ensure the dataset is clean for analysis.
# 2. Basic Data Analysis
Descriptive Statistics: The script prints basic statistics (mean, standard deviation, min, max, etc.) for all numerical columns using df.describe().
Grouping: The data is grouped by the species column, and the mean of each numerical column is calculated for each species. This helps identify differences between the species.
# 3. Data Visualization
The code uses matplotlib and seaborn to create four types of visualizations:

# 4. Line Chart: Shows the trend of sepal length for the first 30 samples.
Bar Chart: Compares the average petal length for each species.
Histogram: Displays the distribution of sepal width values.
Scatter Plot: Visualizes the relationship between sepal length and petal length, colored by species.
All plots are customized with titles, axis labels, and legends for clarity.

# 5. Error Handling
The entire data loading and analysis process is wrapped in a try...except block. If any error occurs (such as a missing library or data issue), a clear error message is printed instead of crashing the program.

# 6. Summary:
This project provides a simple, end-to-end example of loading, cleaning, analyzing, and visualizing a dataset in Python, with robust error handling and clear, well-labeled plots.
