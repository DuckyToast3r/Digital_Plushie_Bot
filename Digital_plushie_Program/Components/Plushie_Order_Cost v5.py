def print_order(del_pick):
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "click and collect":
        print("Your order is for click and collect")
        print(f"Customer Name:{customer_details['name']} \nCustomer Phone:{customer_details['phone']} ")
    
    elif del_pick == "delivery":
        print ("Your order is for delivery a $9.00 delivery charge applies")
        total_cost = total_cost + 9
        print(f"Customer Name:{customer_details['name']} \nCustomer Phone:{customer_details['phone']} \nCustomer Adress:{customer_details['house']} {customer_details['street']} {customer_details['suburb']}  ")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print ("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")