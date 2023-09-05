<h1>Mean Value Imputation:</h1>
    <p>Mean value imputation is a common method for handling missing data in numerical variables. This technique involves replacing missing values with the mean (average) of the observed values for that specific variable. Here's an explanation of this method along with its advantages and disadvantages:</p>

<h2>Advantages:</h2>
    <ol>
    <li><strong>Preserves Data Structure:</strong> Mean imputation is a simple technique that doesn't alter the overall distribution or structure of the data significantly. It keeps the same mean and standard deviation, which can be crucial in certain statistical analyses.</li>

  <li><strong>Useful for Missing Completely at Random (MCAR) Data:</strong> When data is missing completely at random, meaning the probability of missingness is unrelated to the observed or unobserved data, mean imputation can produce unbiased estimates.</li>
    </ol>

<h2>Disadvantages:</h2>
  <ol>
    <li><strong>Doesn't Account for Relationships:</strong> Mean imputation does not consider any relationships or correlations that the variable may have with other variables. It assumes that missing values are missing completely at random, which might not be the case in reality.</li>

  <li><strong>Impacts Distribution:</strong> Mean imputation can distort the distribution of the variable, especially if the missing data is not missing completely at random. It can lead to biased results, especially in predictive modeling where the relationship between variables is crucial.</li>

  <li><strong>Inappropriate for Categorical Data:</strong> Mean imputation is designed for numerical data. Using it for categorical variables doesn't make sense, as you can't calculate the mean of categories.</li>
    </ol>

<br><br>
<hr>
<br><br>

<h1>Median Value Imputation:</h1>
    <p>
        Median value imputation is a technique used to handle missing data in numerical variables by replacing the missing values with the median (middle value) of the observed data for that specific variable. Here's how it works:
    </p>
    
  <h2>Advantages:</h2>
    <ol>
      <li><strong>Preserves Data Distribution:</strong> Median imputation is a non-parametric method, meaning it does not assume any specific data distribution. This can be advantageous when dealing with variables that do not follow a normal distribution. Unlike mean imputation, which can be sensitive to outliers, median imputation is more robust in this regard.</li>
        
        
  <li><strong>Resistant to Extreme Values:</strong> Since the median is less affected by extreme values (outliers) in the data compared to the mean, median imputation can produce more reliable results when outliers are present in the dataset.</li>
    </ol>
    
  <h2>Disadvantages:</h2>
    <ol>
  <li><strong>Reduces Variability:</strong> While median imputation is robust to outliers, it may introduce bias and underestimate the true variability in the data, especially if the missing data is not missing at random. This can impact the accuracy of statistical analyses and machine learning models.</li>
        
  <li><strong>Loss of Information:</strong> By replacing missing values with a single constant (the median), you lose information about the reasons for missing data, potentially obscuring underlying patterns or trends in the dataset.</li>
    

