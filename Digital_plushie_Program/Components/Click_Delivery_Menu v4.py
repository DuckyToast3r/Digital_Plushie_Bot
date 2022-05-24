#Menu so that the user can choose click and collect or delivery

#Bug - need to make it so it only accepts only 1 and 2

print("Is your order for click and collect or delivery?")

print("For click and collect please enter 1")
print("For delivery please enter 2")    



low = 1
high = 2

while True:
    try:
        delivery = int(input())

        if delivery == 1:
            print("Click and Collect") 
            break

        elif delivery == 2:
            print ("Delivery")  
            break  
        
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")