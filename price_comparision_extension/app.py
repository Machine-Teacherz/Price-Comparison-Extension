from modules.e_bay import e_bay
from modules.etsy import etsy
from modules.newegg import newegg
from modules.walmart import walmart
import json
import csv
import datetime




def get_prices():

    user = None
    now = datetime.datetime.now()

    def what_do_u_want():
        choice = input(f'what do you want to do {user}?\n - (n)ew search?\n - (v)iew my favorite?\n - (s)ign out\n > ').lower()
        if choice == 'n':
            new_search()
        elif choice == 'v':
            view_my_fav()
        elif choice == 's':
            main_nav()

    def new_search():
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
            writer.writerows([[user,newlist[choice_pro-1].title,newlist[choice_pro-1].link, newlist[choice_pro-1].website, newlist[choice_pro-1].price, now]])


    def view_my_fav():
        with open('../saves.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]

            print('product id , -------product name------- , ---website--- , ---price--- , ---date--- \n')
            y = False
            for i in new_list:
                if user == i[0]:
                    print(f'{i}, {i[1]} from {i[3]} and it was {i[4]}$ , last cheak was in: {i[5]}\n')
                    y = True
            if not y:
                print('your favorite still empty.. :(')
            
            choice = input('want to edit your fav?\n - (d)elete products\n - (r)e cheak product price\n\n (n)o thank you..').lower()
            while choice not 'n':
                if choice == 'd':
                    choice_pro_id = input('insert your product id : ')
                    del new_list[choice_pro_id]
                    print('done!')
                

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

# def save_choice(list):



if __name__ == '__main__':
    # print(get_prices('apple watch'))
    get_prices()