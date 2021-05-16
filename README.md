Data Science Salary Estimator:Project Overview



 
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

Code and Resources Used

•	Python Version: 3.9
•	Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
•	For Web Framework Requirements: pip install -r requirements.txt
•	Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
•	Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
•	Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

Parsed numeric data out of salary
Made columns for employer provided salary and hourly wages
Removed rows without salary
Parsed rating out of company text
Made a new column for company state
Added a column for if the job was at the company’s headquarters
Transformed founded date into age of company
Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
Column for simplified job title and Seniority
Column for description length

EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.



![image](https://user-images.githubusercontent.com/73906550/118390260-cf756a80-b636-11eb-8106-8bb0084d6c27.png)
![image](https://user-images.githubusercontent.com/73906550/118390304-faf85500-b636-11eb-9698-e649329cbf3a.png)

![image](https://user-images.githubusercontent.com/73906550/118390312-021f6300-b637-11eb-84c7-e2dfee71b86b.png)
![image](https://user-images.githubusercontent.com/73906550/118390319-0cd9f800-b637-11eb-9542-7954f8b53ec6.png)

![image](https://user-images.githubusercontent.com/73906550/118390322-14999c80-b637-11eb-8a12-072f1feaf4cf.png)


Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

Random Forest : MAE = 11.22
Linear Regression: MAE = 18.86
Ridge Regression: MAE = 19.67
Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
