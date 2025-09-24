import pandas as pd
import re

#  All the functions needed here 

#Task 1: Remove duplicates 

def remove_Duplicates(data_set):
    df_clean = data_set.drop_duplicates()
    return df_clean

#Task 2: Checking Email validation
def Email_validation(data_set):
    
    # data_set['Email'].dropna()
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')
    
    data_set.loc[:, 'Email'] = data_set['Email'].fillna('') # Replace NaN with empty string   

    df_valid_emails = data_set[data_set['Email'].apply(lambda email: bool(email_pattern.match(email)))]
    return df_valid_emails.reset_index(drop = True)


#Task 3: Converting them into new csv 
def csv_convertor(data_set, name):
    data_set.to_csv(name , index = False)
    print(f"CSV saved successfully at: {name}")



#Main Operation Start from here
new_data = pd.read_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 1\company_leads.csv")

print("RAW DATA")
print(new_data)                                 #Showing the raw data without any operations



cleaned_data = remove_Duplicates(new_data)      #Removing duplicates
cleaned_data_2 = Email_validation(cleaned_data) #Removing Entries with invalid format of Email address 


#Converting the custom and cleaned data back to csv format 
csv_convertor(cleaned_data_2 , r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 1\Clean_customers.csv")

#Done