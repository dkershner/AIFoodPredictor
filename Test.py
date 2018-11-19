import Food_User_Class as f
import DataProcessor as d

testUser = f.user("test")
names = ["Milk and milk products excluding cheese", "Cheese", "Fish", "Eggs"]
quantities = [1700, 110, 80, 1]
itemsToAdd = f.create_list_of_items(names, quantities)
testUser.add_lst_of_items(itemsToAdd)

dataProcessor = d.DataProcessor()
dataProcessor.predictAmounts(testUser)
