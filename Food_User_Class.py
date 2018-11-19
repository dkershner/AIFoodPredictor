import time

class user:
    def __init__(self, name):
        self.name = name
        self.fridge = []
        self.last_log_in = time.time()
        self.avg_diff = {}

    def add_lst_of_items(self, lst):
        date = time.time()
        for x in lst:
            x.buy_date = date
            x.name = x.name.lower()
            self.fridge +=[x]

    def check_fridge_for_lst_items(self, lst):
        '''
        Checks the items in the inputed list lst.
        If the item is in the fridge list it will add it to the return list
        Returns any items found in the fridge
        '''
        retlst = []
        for x in lst:
            if x in self.fridge:
                retlst += [x]
        return retlst

    def update_fridge_quantity(self):
        '''
        Asks the user how much of each item they have left in their fridge"

        Returns the items that are no longer left in the fridge
        '''
        date = time.time()
        retlst = []
        for i in self.fridge:
            days = date - i.buy_date
            days = int(days//86400)
            x = float(input("How much do you have left of your " + i.name + "?"))
            i.quantity = x
            if x == 0.0:
                days = int(input("How many days ago did you run out " + i.name + "?"))
            else:
                days = 0
            self.update_usage(i, days)

        #self.remove_empty_items()

    def remove_empty_items(self):
        self.fridge = list(filter(self.itemIsEmpty, self.fridge))

    def itemIsEmpty(self, item):
        return item.get_quantity() != 0


    def update_usage(self, item, used_days):
        date = time.time()//86400
        quantity = item.initial_quant - item.quantity
        diff_days = date - used_days - item.buy_date//86400
        diff_value = quantity / diff_days
        diff_value *= 7
        diff_value -= item.initial_quant
        self.avg_diff[item.name.lower()] = diff_value


class item:
    def __init__(self, name, quant, buy_date = 0, days = 0):
        '''
        name - name of item
        quantity - quantity of item
        use_date - date that the item quantity should last till
        '''
        self.name = name
        self.initial_quant = quant
        self.quantity = quant
        #How many days the agent thinks it will take to use the
        #initial quantity of this item
        self.use_days = days
        self.buy_date = buy_date

    def get_use_date(self):
        return self.use_date

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def __eq__(self,itm):
        return self.name == itm.get_name()

def create_list_of_items(names, quants):
        '''
        Accepts:
        names - a list of strings
        quants - a list of each item quantity for each item

        NOTE: the names and quant list should be Parallel to work correctly

        Returns a list of items
        '''
        retlst = []
        if len(names) != len(quants):
            return
        date = time.time()
        for x in range(len(names)):
            itm = item(names[x], quants[x])
            retlst += [itm]

        return retlst
