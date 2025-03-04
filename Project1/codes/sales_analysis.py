import pandas as pd
import matplotlib.pyplot as plt
from manage_input import manage_input, category

df = pd.read_csv('sales_data.csv', index_col=0)
df['total spend'] = df['price'] * df['quantity']  # Adding Total Spend Column in the Dataframe

''' Accessing The categories Customers'''

categories_cus = df[df['category'] == category] # Filtering the categories customers

cate_cus_dict = {"age" : "total_spend"} # Creating a dictionary for categories customers ages and total spneds

for index, i in enumerate(list(categories_cus['customer_age'])): # using for loop to marging multiple same ages in one key
    if str(i) in cate_cus_dict.keys():
        updated_value = cate_cus_dict[str(i)] + categories_cus.iloc[index, 8]
        update = {str(i) : updated_value.round(2)}
        cate_cus_dict.update(update)
    else:
        cate_cus_dict[str(i)] = categories_cus.iloc[index, 8]
    
cate_single_age = list(set(categories_cus['customer_age'])) # using set to sort the ages and remove multiple age
cate_sorted_spend = list()
for i in cate_single_age:  # using for loop to sort the spends as same as the ages for accurate plot
    value = cate_cus_dict[str(i)]
    cate_sorted_spend.append(value)
    
plt.title("The Plot shows The ages of the customer and their spends \nin categories products in a online shop")
plt.xlabel("Ages of the Customers(years)")
plt.ylabel("Amount of Money(USD)")
plt.scatter(cate_single_age,cate_sorted_spend) # creating a plot that shows the ages and their spends
plt.show()