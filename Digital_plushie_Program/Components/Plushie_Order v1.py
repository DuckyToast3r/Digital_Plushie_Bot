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

# ask for total numberof pizzas for order
num_plushie = 0

num_plushie = int(input("How many plushies do you want to order? "))

print(num_plushie)
#choose manga from menu
print("Please choose your plushies by entering the number from the menu")
for item in range(num_plushie):
    while num_plushie > 0:
        manga_ordered = int(input())
        order_list.append(plushie_names[manga_ordered])
        order_cost.append(plushie_prices[manga_ordered])
        num_plushie =  num_plushie-1
    
print(order_list)
print(order_cost)





#countdown untill all pizzas are ordered