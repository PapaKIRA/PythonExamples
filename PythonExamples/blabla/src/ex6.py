'''
Created on Nov 15, 2012

@author: Andrei
'''

fridge = { "beer":"This is beer", "Milk":"This is Milk" ,"lemon":"LemonASDF" , "Juice":"JUICEE"}
 
try: 
    
    wrongKey = fridge["Beer"]
    
except KeyError:
    print( "We are out of beer") 


    

try:
    
    goodKey = fridge["Milk"]
    
except KeyError:
    print( "We are out of Milk")