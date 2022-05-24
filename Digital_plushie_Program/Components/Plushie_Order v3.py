def order_manga():
    # Ask for total number of food for order
    num_manga = 0 
    while True:
        try:
            num_manga = int(input("How many different manga(s) would you like to order? "))
            if num_manga >=1: 
                break
            else:
                print("Please enter a natural number")
        except ValueError:
            print("That is not a valid number")   
            print("Please enter a valid natural number ")
        #Choose food from menu
    for item in range(num_manga):
        while num_manga > 0:
            while True:
                try:
                    manga_ordered = int(input("Please choose your manga(s) by entering the number from the menu "))
                    if manga_ordered >= 1 and manga_ordered <= 12:
                        break
                    else:
                        print("Your manga order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")   
                    print("Please enter a number between 1 and 12") 
            manga_ordered = manga_ordered - 1
            order_list.append(manga_names[manga_ordered])
            order_cost.append(manga_prices[manga_ordered])
            print("{} ${:.2f}" .format(manga_names[manga_ordered],manga_prices[manga_ordered]))
            num_manga = num_manga - 1
