import pandas as pd

file_paths = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

# After running the list comprehension, df_list would contain: 
# df_list = [DataFrame_1, DataFrame_2]
df_list = [pd.read_csv(file) for file in file_paths]
combined_df = pd.concat(df_list, ignore_index=True)

filtered_df = combined_df[combined_df['product'] == 'pink morsel']
filtered_df = filtered_df.reset_index(drop=True)

filtered_df['price'] = filtered_df['price'].replace('[\$, ]', '', regex=True).astype(float)

filtered_df['sales'] = filtered_df['price'] * filtered_df['quantity']

final_df = filtered_df[['sales', 'date', 'region']]

final_df.to_csv('data/formatted_output.csv', index=False)
print(final_df)