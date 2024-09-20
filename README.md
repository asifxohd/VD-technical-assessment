# Technical Assessment Solutions

## Description

This repository contains solutions for a technical assessment involving web scraping, CSV data cleaning, Django model methods, request rate limiting, data aggregation, and finding duplicates in an array.

## Requirements

Make sure you have Python 3 and above installed. Install the necessary packages by running:
#!/bin/bash

# Clone the repository
```
git clone https://github.com/asifxohd/VD-technical-assessment.git

```
# Navigate into the project directory
```
cd VD-technical-assessment
```

# Create a virtual environment
```
python3 -m venv venv_name
```

# Activate the virtual environment
# For macOS/Linux
```
source venv_name/bin/activate
```

# For Windows (use in PowerShell)
```
.\venv_name\Scripts\Activate
```

# Install the required packages
```
pip install -r requirements.txt
```

## Assessment Questions

### Q1: Web Scraping Script

For Question 1, go to `scrape_news.py`.

1. Configure the link you want in the `cnn_url` variable.
2. Run the script using the following command:

```
   python scrape_news.py
```

### Q2: CSV Data Cleaning Script

For Question 2, go to `user_data_cleaner.py`.

1. Use the `user_data.csv` file for testing, which contains the necessary data for the script.
2. Run the script using the following command:

```
   python user_data_cleaner.py
```



### Q3: Django Model Method for Top Customers

For Question 3, follow these steps to set up and test the Django model method:

1. **Run the following commands to set up your database:**

```
   python manage.py makemigrations
   python manage.py migrate
```
```
   python manage.py runserver
```
got to  Postman to interact with the API. The following endpoints are available:

Add Customer: POST /customers/ (GET, POST) <br>
Add Order: POST /orders/ (GET, POST)<br>
Retrieve Top Customers: GET /top-customers/ (GET)<br>
Example URL for retrieving top customers:
```
http://localhost:8000/orders/
```

After adding data, you can check the top customers by accessing the /top-customers/ endpoint.


### Q4: Rate Limiter Implementation

For Question 4,
1. go to `rate_limiter.py`.
2. Run the script using the following command:
3. all the details for the testing this will provided in the code snippet in that file 

```
   python rate_limiter.py
```

### Q5: Write a function aggregate_data

For Question 5,
1. go to `aggregate_data.py`.
2. Run the script using the following command:
3. all the details for the testing this will provided in the code snippet in that script 

```
   python aggregate_data.py
```

### Q6: Write a function aggregate_data

For Question 5,
1. go to `find_duplicates_in_a_array.py`.
2. Run the script using the following command:
3. all the details for the testing this will provided in the code snippet in that script 

```
   python find_duplicates_in_a_array.py
```




