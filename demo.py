import pandas as pd
from pandasql import sqldf

# Load the CSV file into a pandas DataFrame
shop = pd.read_csv('files/shops.csv', names=['id', 'shop_name'])
orders = pd.read_csv('files/orders.csv', names=['id', 'shop_id', 'order_name'])

with open('sql/get_orders.sql', 'r') as file:
    query = file.read()

# Apply the query using pandasql
filtered_df = sqldf(query, globals())

# Print the filtered DataFrame
print(filtered_df)
