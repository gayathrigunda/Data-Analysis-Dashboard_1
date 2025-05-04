import pandas as pd 
#step1: Download the dataset
#step2: load the data 
orders_df=pd.read_csv('orders.csv')
credits_df=pd.read_csv('returns.csv')
print("Orders Dataset: ")
print(orders_df.head())
print("\nCredits Dataset: ")
print(credits_df.head())

#step3: standardise column names(lowercase,no spaces)
orders_df.columns=orders_df.columns.str.lower().str.replace(' ','_')
credits_df.columns=credits_df.columns.str.lower().str.replace(' ','_')

#step4: Convert date columns to date time 
orders_df['order_date']=pd.to_datetime(orders_df['order_date'])
credits_df['order_date']=pd.to_datetime(credits_df['order_date'])

#step5: check for missing values 
print("\nMissing values in orders: ")
print(orders_df.isnull().sum())

print("\nMissing values in credits: ")
print(credits_df.isnull().sum())

#step6: Count duplicate values 
duplicate_rows=orders_df.duplicated() 
print("Number of duplicate rows: ",duplicate_rows.sum())

#step7: changing the column name of  credits_df
credits_df.rename(columns={'sub_order_no':'sub_order_num'},inplace=True)

#step8: Drop rows with missing sub order number 
orders_df.dropna(subset=['sub_order_num'],inplace=True)

#step9: Merge on sub_order_number to combine info 
merged_df=pd.merge(orders_df,credits_df,on='sub_order_num',how='left')

#step10: Add a new column to return flag(1=returned,0=not returned)
merged_df['return_flag']=merged_df['reason_for_credit_entry'].notnull().astype(int)

#step11: Save cleaned merged dataset 
merged_df.to_csv('merged_meesho_data.csv',index=False)

#step12: Total orders and returns 
total_orders=len(orders_df)
returned_orders=merged_df['return_flag'].sum() 
return_rate=(returned_orders/total_orders)*100 

print(f"Total orders: {total_orders}")
print(f"Returned orders: {returned_orders}")
print(f"Return rate: {return_rate:.2f}%")

#step13: Create month column and group by month and sum total price 
orders_df['month']=orders_df['order_date'].dt.to_period('M')
monthly_sales=orders_df.groupby('month')['price'].sum() 
print(f"Monthly sales:{monthly_sales}")

#step14: plot_1
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar',color='green')
plt.title("Monthly Sales Trend")
plt.ylabel('Total sales')
plt.xlabel('Month')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show() 

#step15: plot_2 group by state and calculate return rate 
state_return_rate=merged_df.groupby('state')['return_flag'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
bars = plt.bar(state_return_rate.index, state_return_rate.values, color='red')

# Add percentage labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # center of the bar
        height + 0.005,                     # slightly above the bar
        f"{height*100:.1f}%",               # convert to percent and format
        ha='center', va='bottom', fontsize=8
    )
state_return_rate.plot(kind='bar',color='red')
plt.title("Return Rate by state")
plt.ylabel("Return Rate")
plt.xticks(rotation=90)
plt.tight_layout() 
plt.show()
