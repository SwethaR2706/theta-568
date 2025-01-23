import pandas as pd
sales_data =  {
    'TransactionID':[1,2,3,4,5],
    'CustomerID':[101,102,103,104,101],
    'Amount':[250,300,400,500,600],
    'Date':['2025-01-04','2025-01-03','2025-01-05','2025-01-06','2025-01-02']
}
customer_data = {
    'CustomerID':[101,102,103,104],
    'CustomerName':['Swetha','Nikki','Gorre','Keerthi'],
    'Age':[18,19,18,19],
    'City':['Bvrm','Suryapet','Vikarabad','Hyderabad']
}

sales_df=pd.DataFrame(sales_data)
customers_df=pd.DataFrame(customer_data)
print("Sales DataFrame:")
print(sales_df.head())
print("\nShape of sales data:",sales_df.shape)
print("\nSales data statistics:")
print(sales_df.describe())
print("Sales dataframe",sales_df)
print("customers_df",customers_df)
merged_df=pd.merge(sales_df,customers_df,on='CustomerID',how='inner')
print("\nMerged DataFrame:")
print(merged_df)