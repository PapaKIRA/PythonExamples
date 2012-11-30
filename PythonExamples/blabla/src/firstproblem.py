'''
Created on Nov 1, 2012

@author: Andrei
'''
def BuyBread():
    print("BuyBread")
    return "Bread"
def BuyButter():
     print("BuyButter")
     return "Butter"   

Food= []

Food.append( BuyBread() )
Food.append( BuyButter() )
print(Food)
