# import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

def export_to_excel(data_set):
    # Prepare Monthly Data
    data_set['Date'] = pd.to_datetime(data_set['Date'])
    data_set['YearMonth'] = data_set['Date'].dt.to_period('M')
    monthly_data = data_set.groupby('YearMonth', as_index=False)['Revenue'].sum()
    monthly_data.rename(columns={'Revenue': 'Monthly Revenue'}, inplace=True)

    # Prepare Top 5 Customers
    top_customers = (data_set.groupby('CustomerName', as_index=False)['Revenue']
                     .sum()
                     .sort_values(by='Revenue', ascending=False)
                     .head(5))
    top_customers.rename(columns={'Revenue': 'Total Revenue'}, inplace=True)

    # Total Revenue (single value DataFrame)
    total_rev_df = pd.DataFrame({'Total Revenue': [data_set['Revenue'].sum()]})

    # Write to Excel with multiple sheets
    with pd.ExcelWriter("sales_report.xlsx", engine='openpyxl') as writer:
        total_rev_df.to_excel(writer, sheet_name="Summary", index=False)
        monthly_data.to_excel(writer, sheet_name="Monthly Revenue", index=False)
        top_customers.to_excel(writer, sheet_name="Top Customers", index=False)

    print("✅ Excel report generated: sales_report.xlsx")





#  All the functions needed here 
#Task 1: Total Revenue 

def total_rev(data_set):
    print("Total Revenue :",data_set['Revenue'].sum())

#Task 2: Monthly revenue trend

def monthly_rev(data_set):
    print("Monthly revenue :")
    data_set['Date'] = pd.to_datetime(data_set['Date'])
    data_set['YearMonth'] = data_set['Date'].dt.to_period('M')
    monthly_data = new_data.groupby(['YearMonth'] , as_index = False)['Revenue'].sum()
    monthly_data.rename(columns = {'Revenue':'Monthly Revenue'}, inplace = True)
    print(monthly_data)
#Task 3: Top 5 customers

def top_customer(data_set , number):
    print(f"Top {number} customers are :")
    data = ((data_set.groupby(['CustomerName'], as_index = False)['Revenue'].sum().sort_values(by = 'Revenue', ascending=False).head(number)))
    data.rename(columns = {'Revenue':'Total_Revenue'} , inplace = True)
    print(data)

#Task 4: Ploting sales trend

def plotting(data_set):

    #Converting the date into YYYY/MM format  
    data_set['Date'] = pd.to_datetime(data_set['Date'])
    data_set['YearMonth'] = data_set['Date'].dt.to_period('M')
    monthly_data = new_data.groupby(['YearMonth'] , as_index = False)['Revenue'].sum()
    monthly_data.rename(columns = {'Revenue':'Monthly Revenue'}, inplace = True)


    #Plotting the data into graph 

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data['YearMonth'].astype(str), monthly_data['Monthly Revenue'], marker='o', linestyle='-')
    plt.title('Monthly Revenue Trend (2025)')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#Main operation start from here 


new_data = pd.read_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 2\sales_data.csv")
print("RAW DATA")
print(new_data)   

total_rev(new_data)         #Total Revenue 
monthly_rev(new_data)       #Monthly Revenue 
top_customer(new_data , 5)  #Top n customers
plotting(new_data)

export_to_excel(new_data)