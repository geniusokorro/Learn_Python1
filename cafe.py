'''
Study Notes 
another way to declare a dictionary is from a list but with keys
stock = dict( 1 = 'Beans'...) won't work as int cannot be assigned to string
stock = dict( food1 = 'Beans', food2 = 'Rice', food3 = 'Spaghetti', food4 = 'Sauce-de-gombo')
##to add to dictionary:::
name_of_dict["new_key"] = "new_value"
##pop from a dictionary:::
declare_variable = dict_name.pop('key_to_pop')
##iterate through a dictionary
for i in dict_name.keys():
for i in dict_name.values():
for i,j in dict_name.items()

# num_list = ['1','5','8','14','25','31']
# new_num_list_ints = [int(element)for element in num_list]
# print(new_num_list_ints)
'''

print("Welcome to the total stock calculator for the resturant 🥧")
#Menu list holding all the products that are sold
menu = ['Beans', 'Rice', 'Spaghetti', 'Sauce-de-gombo', 'Fried Plaintain'] #List of menu items
#Stock dictionary with menu items as keys and the quantity as value
stock = {'Beans' : 20,
         'Rice' : 15,
         'Spaghetti' : 4,
         'Sauce-de-gombo' : 9,
         'Fried Plaintain' : 40
        }
#Price dictionary with menu items as keys and their corresponding unit price as values
price = {'Beans' : 40,
         'Rice' : 30,
         'Spaghetti' : 35,
         'Sauce-de-gombo' : 50,
         'Fried Plaintain' : 15
        }
total_stock_val = 0 #Intializing a base variable that will hold the product of each stock and price

#For in loop that loops through the menu list and using each item to call the dictionary item as its key
for item in menu:
        stock_val = (stock[item] * price[item])
        total_stock_val += stock_val #incrementing with the product of each item and price
        
        #printing a table of the products and stock with prices
        print(f"Menu Item: {item} \tStock Quantity: {stock[item]} \tStock Price: £{price[item]}") 
print (f"\nThe total value of the stock is: £{total_stock_val}") #printing the totals