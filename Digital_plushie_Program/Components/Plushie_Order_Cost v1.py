#List of random names
names = ["Mark","Pheobe","Lewis","Micheal","Denise","Hannah","Marcel","Jerome","Grace","Tara"]

#List of plushie Names
plushie_names = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen','Kaguya Sama','Demon Slayer',
    'Spy X Family','Aharen-San','Arifureta','Rising of The Shield Hero','Bofari' ]
#List of plushie Prices
plushie_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50,13.50] 


order_list = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen']
order_cost = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50]


count = 0
for item in order_list:
    print("Ordered:{}  Cost${:.2f}".format(item,order_cost[count]))
    count = count+1
