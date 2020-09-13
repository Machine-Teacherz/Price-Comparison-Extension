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
        print('plaese wait...\n')
        all_objects = e_bay(product)
        newlist = sorted(all_objects, key=lambda x: x.price)
        for i in range(len(newlist)):
            print(i+1, newlist[i])
        sure = input('\nwant to save any of them? (y)es or (n)o? ').lower()
        while True:
            if sure == 'y':
                choice_pro = int(input('witch one you want to save? : '))
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

        with open('../saves.csv', 'w') as writeFile:

            writer = csv.writer(writeFile)

            writer.writerows(last_list)   
            writer.writerows(new_list)   

        what_do_u_want()
    

    def sign_up():
        global user
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
                user = input('\nwhat is your name? : ')
                y = False
                for i in new_list:
                    if user in i:
                        password = input('your password : ')
                        if password == i[1]:
                            print(f'\nWelcome back {user}.. :)')
                            y = True
                        else:
                            print('wrong password!!')
                            continue
                if y:
                    break
                else:
                    print('user not found!')
                    continue
        what_do_u_want()

    def main_nav():
        while True:
            first = input('\nsign (in) OR sign (up)?').lower()
            if first == 'in':
                sign_in()
                break
            elif first == 'up':
                sign_up()
                break


    print('\nWelcome to Price-Compersion-App\n')
    main_nav()




if __name__ == '__main__':
    # print(get_prices('apple watch'))
    get_prices()
