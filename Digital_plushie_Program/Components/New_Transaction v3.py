def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another order? or exit?")
    print ("To start another order enter 1")
    print ("To exit the BOT enter 2")
    confirm = val_int(LOW, HIGH, question)
       
    if confirm == 1:
        print ("New Order")  
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
                

    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()
