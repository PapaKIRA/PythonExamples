'''
Created on Nov 13, 2012

@author: Andrei
'''

fridge = { "Milk":"This is milk", "Cheese":"Tasty Cheese", "Butter":"Peanut butter"}
food_sought = "Butter"
for foodKey in fridge:  #foodkey is a variable in the for loop.You can put anyword besides fridge,food_sought
    print("\nlooking at : %s", foodKey)
    if foodKey == food_sought:
        print("key: %s \tValue: %s"%(foodKey, fridge[food_sought] ))
        break
else:
    print("it was not there")