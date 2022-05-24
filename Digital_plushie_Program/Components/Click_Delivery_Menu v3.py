#Menu so that the user can choose click and collect or delivery

print("Is your order for click and collect or delivery?")

print("For click and collect please enter 1")
print("For delivery please enter 2")    

delivery = int(input())
if delivery == 1:
    print("Click and Collect") 

elif delivery == 2:
    print ("Delivery")    

else:
    print ("That was not a valid input")