from modules.e_bay import e_bay
from modules.etsy import etsy
from modules.newegg import newegg
from modules.walmart import walmart
import json
import csv


def get_prices():
    user = input('what is your name? : ')
    product = input('what are you looking for? : ')
    all_objects = e_bay(product)
    newlist = sorted(all_objects, key=lambda x: x.price)
    for i in range(len(newlist)):
        print(i+1, newlist[i])
    choice = int(input('witch one you want to save? : '))
    print(newlist[choice-1])
    
    with open('saves.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows([[user,newlist[choice-1].link, newlist[choice-1].website]])

# def save_choice(list):



# if __name__ == '__main__':
#     print(get_prices('apple watch'))