import random
from random import randint 

#List of random names
names = ["Mark","Pheobe","Lewis","Micheal","Denise","Hannah","Marcel","Jerome","Grace","Tara"]

def welcome(): #define function (welcome is the name of the function)
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message 
    Parameters:None
    Returns:None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome To Manga Mate ***")
    print("*** My name is",name,  "***")
    print("*** I will be here to help you order your Manga ***")




















def main():
    
     '''
    Purpose: To run all functions 
    Parameters:None
    Returns:None
    ''' 
welcome()


main()