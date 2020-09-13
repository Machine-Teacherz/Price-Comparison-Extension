from modules.e_bay import e_bay
from modules.etsy import etsy
from modules.newegg import newegg
from modules.walmart import walmart
import csv
import datetime
import sys


user = None

def get_prices():

    
    # now = datetime.datetime.now()

    def what_do_u_want():
        choice = input(f'\n\nwhat do you want to do {user}?\n - (n)ew search?\n - (v)iew my favorite?\n - (s)ign out\n - (ex)it\n > ').lower()
        while True:
            if choice == 'n':
                new_search()
                break
            elif choice == 'v':
                view_my_fav()
                break
            elif choice == 's':
                main_nav()
                break
            elif choice == 'ex':
                sys.exit("\nThank you for using our tool.. :)")
            
            choice = input(f'\n\nwhat do you want to do {user}?\n - (n)ew search?\n - (v)iew my favorite?\n - (s)ign out\n - (ex)it\n > ').lower()

    def new_search():
        global user
        product = input('\nwhat are you looking for? : ')
        print('\nplaese wait...')
        all_objects = e_bay(product)
        newlist = sorted(all_objects, key=lambda x: x.price)
        for i in range(len(newlist)):
            print(i+1, newlist[i])
        sure = input('\nwant to save any of them? (y)es or (n)o? ').lower()
        while True:
            if sure == 'y':
                choice_pro = int(input('\nwitch one you want to save? : '))
                print(newlist[choice_pro-1])

                with open('../saves.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerows([[user,newlist[choice_pro-1].title,newlist[choice_pro-1].link, newlist[choice_pro-1].website, newlist[choice_pro-1].price, datetime.datetime.now()]])
                print('\n add to your favorite.. :)')
 