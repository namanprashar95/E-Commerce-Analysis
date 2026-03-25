import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_analysis.csv")
# top 10 rows of the dataset
print(df.head(10))
# information about the dataset
print(df.info())
# description of dataset
print(df.describe())
# shape of the dataset
print(df.shape)
# columns of the dataset
print(df.columns)
# value count of each product category
print(df["Product_Category"].value_counts())
# total sales of each product category can be given by price - discount * unit sold
df["Total_Sales"] = (df["Price"] - df["Discount"]) * df["Units_Sold"]
print(df["Total_Sales"])
# new column total sales is added to the dataset
print(df.head(10))
# total sales of each product category
total_sales_by_category = df.groupby("Product_Category")["Total_Sales"].sum()
print(total_sales_by_category)
# top 5 products with highest sales
top_5_products = df.nlargest(5, "Total_Sales")
print(top_5_products)
# average discount given for each product category
average_discount_by_mean = df.groupby("Product_Category")["Discount"].mean()
print(average_discount_by_mean)
# create a new profit column by assuming margin of 20% on total sales
df["Profit"] = df["Total_Sales"] * 0.2
print(df["Profit"])
print(df.head(10))
# total sales by product category visualization
total_sales_by_category.plot(kind="bar")
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()
# profit by product category
profit_by_category = df.groupby("Product_Category")["Profit"].sum()
print(profit_by_category)
# profit by product category visualization
profit_by_category.plot(kind="bar")
plt.title("Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.show()
# which product category contributed the most in the revenue?
highest_revenue_category = total_sales_by_category.idxmax()
print(highest_revenue_category)

print("The product category that contributed the most in the revenue is: ", highest_revenue_category)
print("Total sales by most contributing product category is: ",total_sales_by_category[highest_revenue_category])
print("Total profit by most contributing category is: ", profit_by_category[highest_revenue_category])
print("Profit margin vary across categories")
print("Some product categories generate higher sales but lower profits due to high discounting")
print("Focus marketing spend on high profit margin categories to maximise profits")
print("Consider reducing discounts on low profit margin product categories to improve profitability")
print("These insights can help the company to make informed decisions about pricing, marketing, discount strategies to maximize revenue and profits")