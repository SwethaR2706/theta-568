import pandas as pd

sales_data =  {
    'TransactionID':[1,2,3,4,5],
    'CustomerID':[101,102,103,104,101],
    'Amount':[600,700,900,1000,1800],
    'Date':['2025-01-04','2025-01-03','2025-01-05','2025-01-06','2025-01-02']
}
customer_data = {
    'CustomerID':[101,102,103,104],
    'CustomerName':['Swetha','Nikki','Gorre','Keerthi'],
    'Age':[18,19,18,19],
    'City':['Bvrm','Suryapet','Chitrakonda','Vikarabad']
}

sales_df=pd.DataFrame(sales_data)
customers_df=pd.DataFrame(customer_data)

print("Sales DataFrame:")
print(sales_df)
print("\nCustomer DataFrame:")
customers_df