'''
Created on Nov 9, 2012

@author: Andrei
'''
food= []
storeInventory=["Bread","Butter","Jam"]

def BuyBread():
    if "Bread" in storeInventory:
        return "Bread"
    return None

def BuyButter():
    pass

def BuyJam():
    pass

def BuyCake():
    pass

def MAS():
    food.append(BuyBread() )
    food.append(BuyButter() )
    food.append(BuyJam() )
    food.append(BuyCake() )
    
    print("This food is...") 