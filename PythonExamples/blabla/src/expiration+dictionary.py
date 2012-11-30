'''
Created on Nov 6, 2012

@author: Andrei
'''
expiration_date =("milkA","milkB","milkC")
milkA=(24,11,1992)
print("%s %s %s" %(milkA))
milk_carton = {}
milk_carton ["expiration"] = milkA
milk_carton ["fl_oz"] = "2 liter"
milk_carton ["cost"] = 20
milk_carton ["brand_name"] = "Arla"

print(milk_carton.values())

print(milk_carton.get("cost")*6) #multiplies cost by 6
