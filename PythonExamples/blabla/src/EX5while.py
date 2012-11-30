'''
Created on Nov 15, 2012

@author: Andrei
'''

fridge = { "Milk":"This is milk", "Cheese":"Tasty Cheese", "Butter":"Peanut butter"} #dictionary must have explination for every word,otherwise is a list.
food_sought = "Butter"
fridge_list = []
for foodKey in fridge:
    fridge_list.append(foodKey) #adding a text line to allready existing tex
print( fridge_list )    

while fridge_list:
    if fridge_list.pop()==food_sought : #pop=takes each element of the list:milk,butter,cheese
        print( "found it again ")       #and comp with foud_sought and when it finds butter  
        break                           #it prints "found it again"
else:
    print("not found")