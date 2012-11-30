'''
Created on Nov 13, 2012

@author: Andrei
'''
# if(x != y) like in C++ 



MyList = ["apple","orange","lemon", "Juice"]
if("apple" == MyList[0]) :     # == -searches for the exact element in the list
    print("true")
elif("orange" in MyList[1]) :
    print("Orange is the 2nd element in the list")
else :
    print("the element is not in the list")      