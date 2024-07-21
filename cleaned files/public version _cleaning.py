import pandas as pd
import os 


#customer behavior 
file_path= ''
df=pd.read_csv(file_path)



df.dropna( inplace=True)

df.drop(columns=['Search_Result_Exploration', 'Customer_Reviews_Importance', 'Add_to_Cart_Browsing', 
                 'Cart_Completion_Frequency', 'Cart_Abandonment_Factors', 'Saveforlater_Frequency', 
                 'Review_Left', 'Review_Reliability', 'Review_Helpfulness', 
                 'Personalized_Recommendation_Frequency', 'Recommendation_Helpfulness', 
                 'Shopping_Satisfaction', 'Service_Appreciation', 'Improvement_Areas'], inplace=True)


customer_behavior_dtype_conversions = {
    'index': 'int64',
    'Order ID': 'int64',
    'Date': 'datetime64[ns]',
    'Status': 'category',
    'Fulfilment': 'category',
    'Sales Channel': 'category',
    'SKU': 'category',
    'Category': 'category',
    'Size': 'category',
    'ASIN': 'category',
    'Qty': 'int64',
    'currency': 'category',
    'Amount': 'float64'
}

for column, dtype in customer_behavior_dtype_conversions.items():
    if column in df.columns:
        try:
            df[column] = df[column].astype(dtype)
        except ValueError as e:
            print(f"Error converting column {column} to {dtype}: {e}")



print(df.dtypes)

print(df)

os.makedirs('' , exist_ok=True)
cleaned_file_path = ''              
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved to {cleaned_file_path}")



#sales
sales_path= ''
df=pd.read_csv(sales_path)
print(df.dtypes)


df.dropna( inplace=True)

df.drop (columns=['ship-service-level','Style','Courier Status','ship-city','ship-state','ship-postal-code',
        'ship-country','promotion-ids','B2B','fulfilled-by','Unnamed: 22'], inplace=True)

os.makedirs('' , exist_ok=True)
cleaned_file = ''               
df.to_csv(cleaned_file, index=False)
print(f"Cleaned dataset saved to {cleaned_file}")

#delivery
delivery_path= ''
df=pd.read_csv(delivery_path)
print(df.dtypes)

df.dropna( inplace=True)

df.drop(columns= ['Store_Latitude','Store_Longitude','Drop_Latitude','Drop_Longitude','Pickup_Time','Weather'
        ,'Traffic','Vehicle','Delivery_Time'] , inplace=True)




print(df)

os.makedirs('' , exist_ok=True)
cleaned_file = ''               
df.to_csv(cleaned_file, index=False)
print(f"Cleaned dataset saved to {cleaned_file}")


