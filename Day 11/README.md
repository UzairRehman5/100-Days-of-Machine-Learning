<h1>Handling Missing Categorical Data using Univariate Imputation</h1>

Handling missing categorical data using univariate imputation involves filling in missing values in categorical columns based on some statistic or constant value calculated from the non-missing data in the same column. Here's a brief overview of the process:

1. **Identify Missing Values**: First, identify which columns in your dataset have missing categorical values.

2. **Choose an Imputation Strategy**:
   - **Most Frequent Imputation**: This is the most common strategy. It replaces missing values with the most frequent category (mode) in the column.
   - **Constant Imputation**: Here, you replace missing values with a predefined constant, such as "Unknown" or "NA."

3. **Apply the Imputation**:
   - For each column with missing values, use the chosen imputation strategy to fill in the missing values.
   - Be sure to fit the imputer on the training data and use the same imputer to transform both the training and testing datasets to maintain consistency.


Univariate imputation is a straightforward way to handle missing categorical data, but it's important to consider the nature of your data and the potential impact of the imputation strategy on your model's performance. In some cases, more advanced techniques like predictive modeling-based imputation might be necessary for better handling missing categorical values.
