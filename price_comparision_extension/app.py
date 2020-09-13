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
                what_do_u_want()
                break
            elif sure == 'n':
                what_do_u_want()
                break
            sure = input('\nwant to save any of them? (y)es or (n)o? ').lower()


    def view_my_fav():
        choice = None
        new_list = []
        with open('../saves.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]
            
            last_list = []
            for row in csv_reader:
                last_list.append(row)
                for field in row:
                    if field == user:
                        last_list.remove(row)

        while choice != 'n':

            print('\n\nproduct id | -------product name------- | ---website--- | ---price--- | ---date--- \n')
            y = False

            for i in range(len(new_list)):
                if user == new_list[i][0]:
                    print(f'{i} | "{new_list[i][1]}" | from : "{new_list[i][3]}" | and it was by : "{new_list[i][4]}$" | last cheak was in : "{new_list[i][5]}"')
                    y = True
            if not y:
                print('your favorite still empty.. :(')
            
            choice = input('\n\nwant to edit your fav?\n - (d)elete products\n - (r)e cheak product price\n\n (n)o thank you..\n > ').lower()
            
            if choice == 'd':
                choice_pro_id = int(input('insert your product id : '))
                del new_list[choice_pro_id]
                print('done!')
                continue
            # elif choice == 'r':
            #     choice_pro_id = input('insert your product id : ')
