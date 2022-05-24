# Menu for click and collect or delivery
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Click and Collect")
        del_pick = "Click and Collect"
        click_collect_info() 
    elif delivery == 2:
        print ("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick
