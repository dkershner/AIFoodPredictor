from Food_User_Class import *
import DataProcessor as d
import time

date = time.time()

tom = user("Tom")
#what the user alread has in the fridge
names= ["Cheese", "Carcase Meat", "Biscuits and crispbreads", "Soft Drinks"]
quants = [250, 150, 400, 2000]
#what the user wants to buy
shopping_list = ["Alcoholic Drinks", "confectionery", "Flour", "Eggs", "Bread", "Cheese", "Carcase Meat", "Biscuits and crispbreads", "soft drinks"]

lst = create_list_of_items(names, quants)

tom.add_lst_of_items(lst)
for x in lst:
    x.buy_date = date - 5*86400

print("Update fridge")
tom.update_fridge_quantity()
print("Fridge Updated")
print("Values that differ from the dataset")
print(tom.avg_diff)
print("Get shopping list")
print(shopping_list)
dataProcessor = d.DataProcessor()
dataProcessor.predictAmounts(shopping_list, tom)
print("Add shopping items to user's fridge")
