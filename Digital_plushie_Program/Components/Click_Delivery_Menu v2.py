#Bugs 
# Will only work for valid input "d" and "c"
#Does not repeat question when invalid input is enter

#Menu so that the user can choose click and collect or delivery

print("Do you want your order delivered or are you going to click and collect?")

print("For delivery enter d")
print("For click and collect enter c")    

delivery = input ()
if delivery == "d":
    print("Delivery")

elif delivery == "c":
    print ("click and collect")    

else:
    print ("That was not a valid input")
