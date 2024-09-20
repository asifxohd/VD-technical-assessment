# Technical Assessment Solutions

## Description

This repository contains solutions for a technical assessment involving web scraping, CSV data cleaning, Django model methods, request rate limiting, data aggregation, and finding duplicates in an array.

## Contents

1. **Web Scraping**: A script to scrape the titles and URLs of the latest articles from a news website using BeautifulSoup and requests.
2. **CSV Data Cleaning**: A script that reads a CSV file with user data, removes duplicate entries based on `user_id`, filters out invalid email formats, and writes the cleaned data to a new CSV file.
3. **Django Model Method**: Implementation of a method to get the top 5 customers who have spent the most in the last 6 months.
4. **Rate Limiter**: A Python implementation that limits the number of requests a user can make within a given time window, with concurrency handling.
5. **Data Aggregation**: A function to aggregate values from a list of dictionaries based on a specified key and apply an aggregator function.
6. **Finding Duplicates**: A solution to find a duplicate number in an array with O(1) extra space.

## Requirements

Make sure you have Python 3 and above installed. Install the necessary packages by running:
#!/bin/bash

# Clone the repository
git clone https://github.com/asifxohd/VD-technical-assessment.git

# Navigate into the project directory
cd VD-technical-assessment || exit

# Create a virtual environment
python3 -m venv venv_name

# Activate the virtual environment
# Uncomment the line appropriate for your OS

# For macOS/Linux
source venv_name/bin/activate

# For Windows (use in PowerShell)
# .\venv_name\Scripts\Activate

# Install the required packages
pip install -r requirements.txt
