<h1>Feature Engineering for Mixed Variables</h1>

   <h2>Introduction:</h2>
    <p>In this report, we focus on the feature engineering steps performed on the Titanic dataset to handle mixed variables. Mixed variables are those that contain both numerical and categorical elements. Our objective is to transform these mixed variables into structured and informative features that can be used for analysis or modeling.</p>

   <h2>Feature Engineering - 'number' Column:</h2>
    <p>We initiated the feature engineering process by addressing the 'number' column, which presented mixed variable characteristics. The following steps were taken:</p>

   <h3>Step 1: Extracting Unique Values</h3>
    <p>Obtained an array of unique values present in the 'number' column. This exploration revealed the diversity of values in this feature.</p>

   <h3>Step 2: Creating a Numerical Representation ('number_numerical')</h3>
    <p>Converted the 'number' column into integer format, effectively handling both numerical and non-numeric elements. Missing or non-numeric values were coerced into NaN.</p>

   <h3>Step 3: Creating a Categorical Representation ('number_categorical')</h3>
    <p>Introduced a categorical representation for the 'number' column. Categorized 'number' values based on conditions, marking non-numeric or missing values as NaN in the 'number_categorical' column.</p>

  <h2>Feature Engineering - 'Cabin' and 'Ticket' Columns:</h2>
    <p>The 'Cabin' and 'Ticket' columns also presented mixed variable characteristics. Feature engineering steps were taken to address these variables:</p>

  <h3>For the 'Cabin' Column:</h3>
    <p>Extracted the first letter of each entry to create a new 'Cabin_category' column, providing a categorical representation. Extracted numerical values using regular expressions and created a 'Cabin_numerical' column to store the numeric portion of 'Cabin' values.</p>

  <h3>For the 'Ticket' Column:</h3>
    <p>Extracted the first part of each ticket value to create a 'Ticket_category' column. Extracted the numeric part of ticket values and created a 'Ticket_number' column, with non-numeric values converted to NaN.</p>

   <h2>Conclusion:</h2>
    <p>The feature engineering steps performed on the mixed variables in the Titanic dataset have effectively transformed them into structured and informative features. These engineered features provide a more comprehensive representation of the data and can be used for subsequent analysis or modeling tasks. Handling mixed variables is a crucial aspect of data preprocessing, as it ensures that all relevant information is captured and utilized in the analysis process.</p>

