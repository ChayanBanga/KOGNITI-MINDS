import pandas as pd
import matplotlib.pyplot as plt

# Task 1: Total Revenue
def total_rev(data_set):
    print("Total Revenue:", data_set['Revenue'].sum())

# Task 2: Monthly revenue trend
def monthly_rev(data_set):
    print("Monthly revenue:")
    data_set['Date'] = pd.to_datetime(data_set['Date'])
    data_set['YearMonth'] = data_set['Date'].dt.to_period('M')
    
    monthly_data = data_set.groupby(['YearMonth'], as_index=False)['Revenue'].sum()
    monthly_data.rename(columns={'Revenue': 'Monthly Revenue'}, inplace=True)
    
    print(monthly_data)
    monthly_data.to_excel("monthly_revenue.xlsx", index=False)

# Task 3: Top N customers
def top_customer(data_set, number):
    print(f"Top {number} customers are:")
    top_data = (data_set.groupby(['CustomerName'], as_index=False)['Revenue']
                .sum()
                .sort_values(by='Revenue', ascending=False)
                .head(number))
    top_data.rename(columns={'Revenue': 'Total_Revenue'}, inplace=True)
    
    print(top_data)
    top_data.to_excel(f"top_{number}_customers.xlsx", index=False)

# Task 4: Plotting sales trend
def plotting(data_set):
    data_set['Date'] = pd.to_datetime(data_set['Date'])
    data_set['YearMonth'] = data_set['Date'].dt.to_period('M')
    
    monthly_data = data_set.groupby(['YearMonth'], as_index=False)['Revenue'].sum()
    monthly_data.rename(columns={'Revenue': 'Monthly Revenue'}, inplace=True)

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data['YearMonth'].astype(str),
             monthly_data['Monthly Revenue'],
             marker='o', linestyle='-')
    plt.title('Monthly Revenue Trend (2025)')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# === MAIN PROGRAM START ===

new_data = pd.read_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 3\sales_data.csv")

print("RAW DATA")
print(new_data)

total_rev(new_data)         # Total Revenue
monthly_rev(new_data)       # It will print Monthly Revenue and also store themm into Excel report
top_customer(new_data, 5)   # It will print Top 5 customers and also store themm into  Excel report 
plotting(new_data)          # Plotting
