import pandas as pd
sales_data = [
    {"CustomerID": "C001", "CustomerName": "Alice Smith", "Date": "2025-01-15", "Product": "Laptop", "Quantity": 1, "UnitPrice": 1200, "Revenue": 1200},
    {"CustomerID": "C002", "CustomerName": "Bob Johnson", "Date": "2025-01-20", "Product": "Mouse", "Quantity": 3, "UnitPrice": 25, "Revenue": 75},
    {"CustomerID": "C003", "CustomerName": "Clara Lee", "Date": "2025-02-10", "Product": "Monitor", "Quantity": 2, "UnitPrice": 200, "Revenue": 400},
    {"CustomerID": "C004", "CustomerName": "Daniel Kim", "Date": "2025-02-22", "Product": "Keyboard", "Quantity": 1, "UnitPrice": 75, "Revenue": 75},
    {"CustomerID": "C005", "CustomerName": "Eva Green", "Date": "2025-03-05", "Product": "Laptop", "Quantity": 1, "UnitPrice": 1200, "Revenue": 1200},
    {"CustomerID": "C006", "CustomerName": "Frank Thomas", "Date": "2025-03-15", "Product": "Headphones", "Quantity": 2, "UnitPrice": 100, "Revenue": 200},
    {"CustomerID": "C001", "CustomerName": "Alice Smith", "Date": "2025-04-01", "Product": "Laptop Bag", "Quantity": 1, "UnitPrice": 50, "Revenue": 50},
    {"CustomerID": "C007", "CustomerName": "George Hall", "Date": "2025-04-18", "Product": "Mouse", "Quantity": 4, "UnitPrice": 25, "Revenue": 100},
    {"CustomerID": "C008", "CustomerName": "Hannah Wright", "Date": "2025-05-02", "Product": "Monitor", "Quantity": 1, "UnitPrice": 200, "Revenue": 200},
    {"CustomerID": "C002", "CustomerName": "Bob Johnson", "Date": "2025-05-22", "Product": "Monitor", "Quantity": 2, "UnitPrice": 200, "Revenue": 400},
    {"CustomerID": "C009", "CustomerName": "Ian Clark", "Date": "2025-06-12", "Product": "Laptop", "Quantity": 1, "UnitPrice": 1200, "Revenue": 1200},
    {"CustomerID": "C010", "CustomerName": "Jane Lopez", "Date": "2025-06-18", "Product": "Laptop Bag", "Quantity": 2, "UnitPrice": 50, "Revenue": 100},
    {"CustomerID": "C004", "CustomerName": "Daniel Kim", "Date": "2025-07-10", "Product": "Mouse", "Quantity": 5, "UnitPrice": 25, "Revenue": 125},
    {"CustomerID": "C005", "CustomerName": "Eva Green", "Date": "2025-07-22", "Product": "Keyboard", "Quantity": 1, "UnitPrice": 75, "Revenue": 75},
    {"CustomerID": "C006", "CustomerName": "Frank Thomas", "Date": "2025-08-01", "Product": "Monitor", "Quantity": 1, "UnitPrice": 200, "Revenue": 200},
    {"CustomerID": "C001", "CustomerName": "Alice Smith", "Date": "2025-08-15", "Product": "Mouse", "Quantity": 2, "UnitPrice": 25, "Revenue": 50},
    {"CustomerID": "C002", "CustomerName": "Bob Johnson", "Date": "2025-08-28", "Product": "Headphones", "Quantity": 1, "UnitPrice": 100, "Revenue": 100},
    {"CustomerID": "C003", "CustomerName": "Clara Lee", "Date": "2025-09-01", "Product": "Laptop", "Quantity": 1, "UnitPrice": 1200, "Revenue": 1200},
    {"CustomerID": "C009", "CustomerName": "Ian Clark", "Date": "2025-09-10", "Product": "Keyboard", "Quantity": 1, "UnitPrice": 75, "Revenue": 75},
    {"CustomerID": "C010", "CustomerName": "Jane Lopez", "Date": "2025-09-15", "Product": "Headphones", "Quantity": 1, "UnitPrice": 100, "Revenue": 100}
]

data = pd.DataFrame(sales_data)
data.to_csv(r"C:\Users\chaya\Desktop\internship tasks\Python developer\Task 2\sales_data.csv" , index= False)