Our code includes a DataProcessor class which is responsible for reading the dataset and giving predictions on the amount of food a user
will need, a User class that stores the information for the user including how much they differ from usual amounts of consumption
of certain foods and what food they have in their fridge, and an item class that stores all relevant information about a specific food.
We created a file called ClassDemo to demonstrate running the program. It starts the user with a few items in their fridge and then
prompts them to answer a few questions about how much they have left of each item (these values were chosen randomly for demo purposes).
Next it provides a shopping list that the agent should give estimates for, and you will see it use the data set and the user's
average difference from normal for a given food to predict a quantity of food the user should buy for the next week. This quantity
is always rounded up, and sometimes rounded to a specific amount, such as eggs, which we always round up to the nearest half dozen.
This is due to the fact that it is hard to find eggs in quantities other than multiples of 6.

To run this demo, simply run:
python ClassDemo.py

Feel free to modify the original items in the fridge, the shopping list, or just pick whatever quantities remaining you'd like.
Please note that the items provided must exactly match (not including case) entries in the dataset, as it is hard to distinguish
between such specific entries otherwise.