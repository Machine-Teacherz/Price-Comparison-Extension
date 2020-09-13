from modules.e_bay import e_bay
from modules.etsy import etsy
from modules.newegg import newegg
from modules.walmart import walmart
import json
import csv



def get_prices():

    users = None

    def sign_up():
        with open('users.csv') as csv_file:
        # df = pd.read_csv("../users.csv")
        # exists = df[df.user == user].user.item()
            csv_reader = csv.reader(csv_file, delimiter=',')
            new_list = [[ii for ii in i] for i in csv_reader]
            # x = True
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
        # with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows([[user, password]])
            csv_file.close()
        choice = input('what do want to do?\n - (n)ew search?\n - (v)iew my favorite? ').lower()
        if choice == 'n':
            new_search()
        elif choice == 'v':
            # view_my_fav()
    
    def new_search():
        product = input('what are you looking for? : ')
        all_objects = e_bay(product)
        newlist = sorted(all_objects, key=lambda x: x.price)
        for i in range(len(newlist)):
            print(i+1, newlist[i])
        choice_pro = int(input('witch one you want to save? : '))
        print(newlist[choice_pro-1])

        with open('saves.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            # writer.writerows([[user,newlist[choice_pro-1].link, newlist[choice_pro-1].website]])s

    while True:
        first = input('in or up?').lower()
        if first == 'in':
            # sign_in()
            break
        elif first == 'up':
            sign_up()
            break

# def save_choice(list):



if __name__ == '__main__':
    # print(get_prices('apple watch'))
    get_prices()