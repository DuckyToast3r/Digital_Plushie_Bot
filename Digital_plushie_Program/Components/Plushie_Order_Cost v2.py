#List of random names
names = ["Mark","Pheobe","Lewis","Micheal","Denise","Hannah","Marcel","Jerome","Grace","Tara"]

#List of Manga Names
manga_names = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen','Kaguya Sama','Demon Slayer',
    'Spy X Family','Aharen-San','Arifureta','Rising of The Shield Hero','Bofari' ]
#List of Manga Prices
manga_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50,13.50] 


order_list = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen']
order_cost = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50]



cust_details = {'name': 'Mark','phone': '218032019830', 'house': '45', 'street': 'Harry', 'suburb' :'Howick'  }

#print("\n",cust_details['name'],"\n",cust_details['phone'], "\n",cust_details['house'],"\n",cust_details['street'], "\n", cust_details['suburb'] )

print("\n Customer Name:{} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{}  Customer Suburb:\n{}".format( cust_details['name'],cust_details['phone'], cust_details['house'],cust_details['street'],  cust_details['suburb'] ))

count = 0
for item in order_list:
    print("Ordered:{}  Cost${:.2f}".format(item,order_cost[count]))
    count = count+1