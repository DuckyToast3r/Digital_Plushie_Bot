
plushie_names = ['Hunter X Hunter','Tokyo Ghoul','Naruto','Black Clover','Jujutsu Kaisen','Kaguya Sama','Demon Slayer',
    'Spy X Family','Aharen-San','Arifureta','Rising of The Shield Hero','Bofari' ]

plushie_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50,13.50] 
def menu():
    number_plushie = 12
    for count in range (number_plushie):
        print("{} {} ${:.2f}"  .format(count+1, plushie_names[count], plushie_prices[count]))

menu()
