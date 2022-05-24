def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print(f"Customer Name:{customer_details['name']} \nCustomer Phone:{customer_details['phone']} \nCustomer Adress:{customer_details['house']} {customer_details['street']} {customer_details['suburb']}  ")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print ("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    