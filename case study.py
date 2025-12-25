#Case Study 2
import numpy as np
#Generate synthetic data
#Store IDs(20 stores)
num_transactions = 1000000
store_ids = np.random.randint(1,21,num_transactions)
#Product IDs
product_ids = np.random.randint(1,101,num_transactions)
#Quantity sold per transaction
quantity_sold = np.random.randint(1,50,num_transactions)
#Price per unit
price_per_unit = np.random.uniform(5,1000,num_transactions)
dates = np.random.choice(np.arange('2023-01','2024-01',dtype = 'datetime64[D]'),num_transactions)
#Scenario1:Total sales across all stores
#Calculate sales for each transactions
sales = quantity_sold * price_per_unit
#Total sales across all stores
total_sales = np.sum(sales)
print(f"Total sales across all stores:{total_sales:.2f}")
#Scenario2: Sales by store
#aggregrate sales by store
unique_stores,store_indices = np.unique(store_ids,return_inverse = True)
sales_per_store = np.zeros(len(unique_stores),dtype = 'f4')
np.add.at(sales_per_store,store_indices,sales)
#Combine store sales data
store_sales = np.array(list(zip(unique_stores,sales_per_store)),dtype= [('Store_ID','i4'),('Total_sales','f4')])
top_stores = np.sort(store_sales,order = 'Total_sales')[::-1][:5]
print("Top 5 Stores by Sales:")
for store,sales in top_stores:
    print(f"Store ID:{store},Total Sales:{sales:.2f}")

#Scenario3 : Sales by product
unique_products,product_indices = np.unique(product_ids,return_inverse = True)
sales_per_product = np.zeros(len(unique_products),dtype = 'f4')
np.add.at(sales_per_product,product_indices,sales)
#Combine product sales data
product_sales = np.array(list(zip(unique_products,sales_per_product)),dtype = [('Product_ID','i4'),('Total_sales','f4')])
top_products = np.sort(product_sales,order= 'Total_sales')[::-1][:5]
print("Top 5 Best selling Products:")
for product,sales in top_products:
    print(f"Product ID:{product},Total sales:{sales:.2f}")

#Scenario 4 : Sales Trend over time
transaction_month = dates.astype('datetime64[M]')
unique_months,month_indices = np.unique(transaction_month,return_inverse = True)
monthly_sales = np.zeros(len(unique_months),dtype = 'f4')
np.add.at(monthly_sales,month_indices,sales)
monthly_sales_trends = np.array(list(zip(unique_months,monthly_sales)),dtype = [("Month","datetime64[M]"),("Total_sales","f4")])
print("Monthly sales trends:")
for month,sales in monthly_sales_trends:
    print(f"{month}:{sales:.2f}")
best_month = monthly_sales_trends[np.argmax(monthly_sales_trends['Total_sales'])]
print(f"Best performing month:{best_month['Month']}with total sales of{best_month['Total_sales']:.2f}")


#Scenario5: Customer Segmentation Based on Spending
#generate synthetic customer IDs
customer_ids = np.random.randint(1000,5000,num_transactions)
#Aggregate total spending per customer
unique_customers,customer_indices = np.unique(customer_ids,return_inverse = True)
total_spending_per_customer = np.zeros(len(unique_customers),dtype ='f4')
np.add.at(total_spending_per_customer,customer_indices,sales)
#Define segmentation thresholds
low_spending_threshold = 5000
medium_spending_threshold = 20000
low_spending_customers = unique_customers[total_spending_per_customer <= low_spending_threshold]
medium_spending_customers = unique_customers[(total_spending_per_customer > low_spending_threshold) & (total_spending_per_customer <= medium_spending_threshold)]
high_spending_customers = unique_customers[total_spending_per_customer > medium_spending_threshold]
print(f"Low spending customers:{len(low_spending_customers)}")
print(f'Medium spending customers:{len(medium_spending_customers)}')
print(f"High spending customers:{len(high_spending_customers)}")

#Scenario 6: Seasonal sales Comparison
#define the data ranges for summer and winter
summer_period = np.isin(dates.astype('datetime64[M]'),['2023-04','2023-05','2023-06'])
winter_period = np.isin(dates.astype('datetime64[M]'),['2023-12','2024-01','2024-02'])
summer_sales = np.sum(sales[summer_period])     
winter_sales = np.sum(sales[winter_period])
print(f"Total Summer Sales:?{summer_sales:.2f}")
print(f"Total Winter Sales:?{winter_sales:.2f}")
if summer_sales > winter_sales:
    print("Summer sales are higher than winter sales.") 
elif winter_sales > summer_sales:
    print("Winter sales are higher than summer sales.")
else:
    print("Summer and winter sales are equal.")
#Scenario 7:Sales Perfomance per Store
previous_year_sales = np.random.uniform(100000,1000000,len(store_ids))
sales_growth_percentage = (sales - previous_year_sales)/previous_year_sales * 100
store_growth = np.zeros(len(unique_stores),dtype = 'f4')
np.add.at(store_growth,store_indices,sales_growth_percentage)
store_growth_data = np.array(list(zip(unique_stores,store_growth)),dtype = [('Store_ID','i4'),('Growth_percentage','f4')])
top_growth_stores = np.sort(store_growth_data,order = "Growth_percentage")[::-1][:5]
print("Top 5 stores by year on year growth")
for store,growth in top_growth_stores:
    print(f"Store ID:{store},Growth :{growth:.2f}%")

#Scenario 8: Store Performance based on product categories
product_categories = np.random.choice(["Electronics","Apparel","Groceries","Furniture"],num_transactions)
unique_categories = np.unique(product_categories)
sales_per_category_per_store = np.zeros((len(unique_stores),len(unique_categories)),dtype = 'f4')
for store_idx in range(len(unique_stores)):
    for category_idx,category in enumerate(unique_categories):
        category_sales = sales[(store_indices==store_idx)&(product_categories==category)]
        sales_per_category_per_store[store_idx,category_idx] = np.sum(category_sales)
for store_idx,store in enumerate(unique_stores):
    print(f"\nStore ID:{store}")
    for category_idx,category in enumerate(unique_categories):
        print(f"{category}:?{sales_per_category_per_store[store_idx,category_idx]:.2f}")
                                                                            
# This code simulates a retail sales dataset and performs various analyses such as total sales calculation, sales by store and product, sales trends over time, customer segmentation based on spending, seasonal sales comparison, year-on-year growth analysis, and store performance based on product categories.
# It uses NumPy for efficient data generation and aggregation.  