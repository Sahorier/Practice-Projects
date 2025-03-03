import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/Practice Projects/Project1/resources/sales_data.csv', index_col=0)
df['total spend'] = df['price'] * df['quantity']  # Adding Total Spend Column in the Dataframe

''' Accessing The Electronics Customers'''

electronics_cus = df[df['category'] == 'Electronics'] # Filtering the Electronics customers

elec_cus_dict = {"age" : "total_spend"} # Creating a dictionary for electronics customers ages and total spneds

for index, i in enumerate(list(electronics_cus['customer_age'])): # using for loop to marging multiple same ages in one key
    if str(i) in elec_cus_dict.keys():
        updated_value = elec_cus_dict[str(i)] + electronics_cus.iloc[index, 8]
        update = {str(i) : updated_value.round(2)}
        elec_cus_dict.update(update)
    else:
        elec_cus_dict[str(i)] = electronics_cus.iloc[index, 8]
    
elec_single_age = list(set(electronics_cus['customer_age'])) # using set to sort the ages and remove multiple age
elec_sorted_spend = list()
for i in elec_single_age:  # using for loop to sort the spends as same as the ages for accurate plot
    value = elec_cus_dict[str(i)]
    elec_sorted_spend.append(value)
    
plt.title("The Plot shows The ages of the customer and their spends \nin Electronics products in a online shop")
plt.xlabel("Ages of the Customers(years)")
plt.ylabel("Amount of Money(USD)")
plt.plot(elec_single_age,elec_sorted_spend) # creating a plot that shows the ages and their spends
plt.show()