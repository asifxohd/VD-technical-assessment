import csv
import re

def is_valid_email(email):
    """
    Check if the email address is valid
    """
    pattern = r'^(?!.*\.\.)([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com)$'
    return re.match(pattern, email) is not None


def clean_user_data(input_file, output_file):
    """
    Clean user data by removing duplicates and invalid emails
    """
    seen_user_ids = set()  
    cleaned_data = []

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            user_id = row['user_id']
            email = row['email']
            
            if user_id not in seen_user_ids and is_valid_email(email):
                seen_user_ids.add(user_id)
                cleaned_data.append(row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['user_id', 'email', 'name', 'age', 'city']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

    return cleaned_data


if __name__ == "__main__":
    input_csv = 'user_data.csv'
    output_csv = 'cleaned_user_data.csv'
    
    cleaned_data = clean_user_data(input_csv, output_csv)
    
    print("Cleaned user data:")
    for row in cleaned_data:
        print(row)
