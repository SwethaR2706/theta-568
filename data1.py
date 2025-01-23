# prompt: create two data frames int the first dataframe product and customer name in the second dataframe product name and price try to join with product name

# DataFrame 1: Products and Customer Name
data1 = {'Product Name': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
        'Customer Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']}
df1 = pd.DataFrame(data1)

# DataFrame 2: Product Name and Price
data2 = {'Product Name': ['Laptop', 'Mobile', 'Tablet', 'Desktop'],
        'Price': [1200, 800, 300, 1500]}
df2 = pd.DataFrame(data2)

# Merge the two DataFrames based on 'Product Name'
merged_df = pd.merge(df1, df2, on='Product Name', how='inner')  # Use 'inner' join

merged_df