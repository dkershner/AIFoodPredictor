import xlrd
import math
import Food_User_Class

YEAR_COL = 49
UNIT_COL = 5
CAT_COL = 1

class DataProcessor:

    def __init__(self):
        wb = xlrd.open_workbook('GroceryData.xlsx')
        sheet = wb.sheet_by_index(1)
        self.data = {}
        self.getData(sheet)

    def getData(self, sheet):
        '''
        Stores all the average usages and units of items in the dataset.
        '''
        for row in range(8,345):
            val = sheet.cell_value(row, CAT_COL)
            if val != '':
                self.data[val.lower()] = (sheet.cell_value(row, YEAR_COL), sheet.cell_value(row, UNIT_COL))

    def predictAmounts(self, sList, user):
        '''
        Takes the user's current fridge and predicts how much more of each item
        they will need for the next week based on our dataset of averages.
        '''
        shoppingList = []
        for x in sList:
            shoppingList.append(x.lower())

        toRemove = []
        for item in user.fridge:
            if item.get_name() in shoppingList:
                need = self.data[item.get_name().lower()]
                averageUse = need[0]
                have = item.get_quantity()
                userAvgDiff = user.avg_diff[item.get_name().lower()]
                predictedNeed = averageUse + userAvgDiff - have
                if predictedNeed <= 0:
                    print("You should have enough ", item.get_name(), " for the next week.")
                else:
                    amount, quant = self.convertToOutput(item.get_name(), predictedNeed, need[1])
                    print("You should buy", amount, "more", item.get_name(), "for the next week.")
                    item.quantity += quant
                toRemove.append(item.get_name())
        for remove in toRemove:
            shoppingList.remove(remove)
        listToAdd = []
        for name in shoppingList:
            need = self.data[name.lower()]
            predictedNeed = need[0]
            if predictedNeed <= 0:
                print("You should have enough ", name, " for the next week.")
            else:
                amount, quant = self.convertToOutput(name, predictedNeed, need[1])
                print("You should buy", amount, "more", name, "for the next week.")
                listToAdd.append(Food_User_Class.item(name, quant))
        user.add_lst_of_items(listToAdd)

    def convertToOutput(self, item, amountNeeded, unit):
        if item == "milk and milk products excluding cheese":
            #round milk to the nearest liter
            liters = amountNeeded / 1000
            amount = int(math.ceil(liters))
            return (str(amount) + "L", amount * 1000)
        elif item == "cheese":
            #round cheese to the nearest 8oz (typical size of a bag of cheese)
            ounces = self.gramsToOunces(amountNeeded)
            amount = int(((ounces // 8) + 1) * 8)
            return (str(amount)  + "oz", self.ouncesToGrams(amount))
        elif item == "fish":
            #round fish to the nearest half pound
            pounds = self.gramsToOunces(amountNeeded) / 16
            amount = ((pounds // .5) + 1) * .5
            return (str(amount) + "lbs", amount)
        elif item == "eggs":
            #round eggs to the nearest half dozen (6)
            amount = int(((amountNeeded // 6) + 1) * 6)
            return (str(amount), amount)
        else:
            if unit == "ml":
                #default round up to nearest 100ml
                amount = int(((amountNeeded // 100) + 1) * 100)
                return (str(amount) + "ml", amount)
            elif unit == "g":
                #default round up to nearest gram
                amount = math.ceil(amountNeeded)
                return (str(amount) + "g", amount)
            else: return


    def gramsToOunces(self, amount):
        return amount * .035274

    def ouncesToGrams(self, amount):
        return amount * 28.3495

    def lbsToGrams(self, amount):
        return amount * 453.592

    def predictDaysRemaining(self, item):
        '''
        Takes an item and predicts how long it will take someone to fully use
        up the quantity they have, based on how much an average person uses
        in a week.
        '''
        percentQuantity = item.get_quantity() / self.data[item.get_name()]
        days = percentQuantity * 7
        return days
