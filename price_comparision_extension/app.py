from modules.e_bay import e_bay
from modules.etsy import etsy
from modules.newegg import newegg
from modules.walmart import walmart
import json
import csv
import datetime


user = None

def get_prices():

    
    # now = datetime.datetime.now()

    def what_do_u_want():
        choice = input(f'what do you want to do {user}?\n - (n)ew search?\n - (v)iew my favorite?\n - (s)ign out\n > ').lower()
        if choice == 'n':
            new_search()
        elif choice == 'v':
            view_my_fav()
        elif choice == 's':
            main_nav()

    def new_search():
        global user
        product = input('what are you looking for? : ')
        print('plaese wait...')
        all_objects = e_bay(product)
        newlist = sorted(all_objects, key=lambda x: x.price)
        for i in range(len(newlist)):
            print(i+1, newlist[i])
        choice_pro = int(input('witch one you want to save? : '))
        print(newlist[choice_pro-1])

        with open('../saves.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows([[user,newlist[choice_pro-1].title,newlist[choice_pro-1].link, newlist[choice_pro-1].website, newlist[choice_pro-1].price, datetime.datetime.now()]])
        what_do_u_want()


    def view_my_fav():
        choice = None
        new_list = []
        with open('../saves.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]

        while choice != 'n':

            print('\n\nproduct id , -------product name------- , ---website--- , ---price--- , ---date--- \n')
            y = False
            # print(new_list)
            # print(user)
            for i in range(len(new_list)):
                if user == new_list[i][0]:
                    print(f'{i}, {new_list[i][1]} from {new_list[i][3]} and it was {new_list[i][4]}$ , last cheak was in: {new_list[i][5]}')
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
            #     if new_list[choice_pro_id][2] == 'e_bay':
            #         new_line = # e_bay link method
            #     elif new_list[choice_pro_id][2] == 'walmart':
            #         new_line = # walmart link method
            #     elif new_list[choice_pro_id][2] == 'newegg':
            #         new_line = # newegg link method
            #     elif new_list[choice_pro_id][2] == 'etsy':
            #         new_line = # etsy link method


                # new_list[choice_pro_id][4],new_list[choice_pro_id][5] = new_line,datetime.datetime.now()
                # continue

                

        what_do_u_want()
    

    def sign_up():
        with open('../users.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]

            while True:
                user = input('what is your name? : ')
                y = False
                for i in new_list:
                    if user in i:
                        print('the name is already taken!!')
                        y = True
                if y:
                    continue
                else:
                    break

            password = input('your password : ')
        with open('../users.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows([[user, password]])
            file.close()
        what_do_u_want()

    
    def sign_in():
        global user
        with open('../users.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]

        while True:
                user = input('what is your name? : ')
                y = False
                for i in new_list:
                    if user in i:
                        print(f'hello {user}.. :)')
                        y = True
                if y:
                    break
                else:
                    print('user not found!')
                    continue
        what_do_u_want()

    def main_nav():
        while True:
            first = input('in or up?').lower()
            if first == 'in':
                sign_in()
                break
            elif first == 'up':
                sign_up()
                break
    main_nav()
# def save_choice(list):



if __name__ == '__main__':
    # print(get_prices('apple watch'))
    get_prices()
