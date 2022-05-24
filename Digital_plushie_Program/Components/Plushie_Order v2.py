# list of pizza names
plushie_names = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen','Kaguya Sama','Demon Slayer',
    'Spy X Family','Aharen-San','Arifureta','Rising of The Shield Hero','Bofari' ]
# list of pizza prices
plushie_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50,13.50] 

#list to store ordered pizzas
order_list =[]
#list to store pizza prices
order_cost =[]

# list to store order cost
def menu():
    number_plushie = 12
    for count in range (number_plushie):
        print("{} {} ${:.2f}"  .format(count+1, plushie_names[count], plushie_prices[count]))

menu()



while True:
    try:
        num_plushie = int(input("How many plushie(s) do you want to order? "))
        if num_plushie >=1:
            break
        else:
            print("Please enter a natural number")
        
    except ValueError:
            print ("That is not a valid number")
            print("Please enter a number a number 1 and 12")

#choose plushie from menu
for item in range(num_plushie):
    while num_plushie > 0:
        while True:
            try:
                plushie_ordered = int(input("Please choose your  by entering the number from the menu" ))
                if plushie_ordered >=1 and plushie_ordered <=12:
                    break
                else:
                     print("Your plushie order must be between 1 and 12")
            except ValueError:
                print("This is not a valid number")
                print("Please enter a number between 1 and 12")
        plushie_ordered = plushie_ordered-1
        order_list.append(plushie_names[plushie_ordered])
        order_cost.append(plushie_prices[plushie_ordered])
        print("{} ${:.2f}" .format(plushie_names[plushie_ordered],plushie_prices[plushie_ordered]))
        num_plushie =  num_plushie-1
    






#countdown untill all pizzas are ordered