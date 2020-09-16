from modules.e_bay import e_bay, e_bay_price
from modules.etsy import etsy, etsy_price
from modules.newegg import newegg, newegg_price
from modules.walmart import walmart, wal_price
import csv
import datetime
import sys

from tkinter import *
from tkinter import ttk, messagebox, font

from face_detection.face_rec import *
from face_detection.face_capture import *

import time
import webbrowser

from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

import schedule
from auto import auto

from PIL import ImageTk, Image
from datetime import datetime

user = 'guest'


def new_window():

    def sign_in():
        global user
        if len(photos_names) > 0:
            person = find_face()
            if person in photos_names:
                user = person
                messagebox.showinfo(title='error', message=f'\nWelcome back {user}.. :)')
                root.destroy()
            else:
                messagebox.showinfo(title='error', message='you are not registered  please sign up first ')
        else:
            messagebox.showinfo(title='error', message='you are not registered  please sign up first ')

        # print(photos_names)

    def sign_up():
        global user
        ti = datetime.now().second
        # print(ti)
        new_user = capture_img()
        user = new_user
        messagebox.showinfo(title='error', message=f'hello {user}')
        root.destroy()

        # if x == False:
        #     user = new_user
        #     root.destroy()
        # else:
        #     messagebox.showinfo(title='error', message='you are already registered')
        #     # sign_in()

    root = Tk()
    root.geometry('310x330')
    root.title('Sign up/in')
    root.config(bg='#204051')
    Label(root, text='Welcome to \nPrice Comparison Extension', font=('Helvetica 18',13, 'bold')).place(x=20,y=10)
    rigister = Button(root, command=sign_up, text='Rigister By Face', font=('Helvetica 18'), width=13, height=2, bg='#e4e3e3', fg="#204051", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=0, column=0, padx=55, pady=75)
    Label(root, text='OR', font=('Helvetica 18',13, 'bold')).place(x=140,y=160)
    login = Button(root, command=sign_in,text='Sign In By Face', font=('Helvetica 18'), width=13, height=2, bg='#e4e3e3', fg="#204051", bd=1, activebackground="#3e646c", activeforeground="pink").grid(row=1, column=0,pady=(0,0))


    def exit_all():
        sys.exit()
    Button(root, text="Exit", command=exit_all).grid(row=5, column=0,pady=10)

    def disable_event():
        pass

    # root.protocol("WM_DELETE_WINDOW", disable_event)

    root.mainloop()
value = None
newlist = []
choice = None
new_list = []
last_listn = []
user_list = []
n_user = True
event = None
minute = None
label_6 = None
counter = False
timeer = 0

def new_window2():
    window = Tk()
    note = ttk.Notebook(window)
    window.geometry('900x500+150+300')
    window.title('Price Comparision Extension')

    search_tap = Frame(note)
    fav_tap = Frame(note)
    ittraion_tap = Frame(note)
    about_us_tap = Frame(note)

    note.add(search_tap, text='Search')
    note.add(fav_tap, text='Favorite')
    note.add(ittraion_tap, text='Iteration')
    note.add(about_us_tap, text='about_us')

    note.pack(expand=1, fill="both")

    global label_6
    label_6 = Label(ittraion_tap)

    def new_search():
        global newlist
        # dele()
        product = by.get()
        if product == '':
            messagebox.showinfo(title='error', message='erorr')
        else:
            all_objects = etsy(product) + newegg(product) + walmart(product)
            newlist = sorted(all_objects, key=lambda x: x.price)
            # time.sleep(10)

            for i in range(len(newlist)):
                search_result.insert(i+1, newlist[i])

            text2 = Listbox(search_tap, width=5, height=1)
            Label(search_tap, text='product number you want to save is: ').place(x=20, y=412)
            b4 = Button(search_tap, text='Save', command=save_to).place(x=330, y=410)
            text2.place(x=270, y=413)

            def onselect(evt):
                global choice
                w = evt.widget
                value = w.curselection()[0]+1
                text2.delete(0, END)
                print('You selected item %d: ' % (value))
                text2.insert(1, value)
                choice = value
                # print(choice)

            search_result.bind('<<ListboxSelect>>', onselect)
            view_my_fav()




    global minute
    minute = StringVar()
    def view_my_fav():
        global new_list
        global last_list
        global user_list
        global n_user
        global user
        lb_f.delete(0, END)
        with open('../../saves.csv', 'r', encoding="utf8") as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',')
            # print(csv_reader)
            new_list = [[ii for ii in i] for i in csv_reader]

            last_list = []
            for i in new_list:
                last_list.append(i)
                for j in i:
                    if j == user:
                        last_list.remove(i)

            user_list = []
            for i in new_list:
                user_list.append(i)
                if i[0] != user:
                    user_list.remove(i)

            if len(user_list) > 0:
                n_user = False
            print(user_list)

            y = False
            for i in range(len(new_list)):
                if user == new_list[i][0]:
                    lb_f.insert(i,f'{new_list[i][1]} | from: {new_list[i][3]} | it was by: {new_list[i][4]}$ | last cheak: {new_list[i][5]}')
                    y = True
            if not y:
                lb_f.insert(1,'your favorite still empty.. :(')
        if len(user_list) > 0:
            entry_1 = Label(ittraion_tap,text=user_list[0][5]).place(x=480,y=157)
        else:
            entry_1 = Label(ittraion_tap, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S")).place(x=480, y=157)


    by = StringVar()
    text = Entry(search_tap,textvariable=by, width=30).grid(row=1,column=1,pady=(36,40),padx=(0,190))
    Label(search_tap, text='what your looking for?').grid(row=1,column=1,pady=(0,0),padx=(0,600))

    search_result = Listbox(search_tap,height=22,width=145,font="Helvetica")
    Label(search_tap,text='Results:').place(x=0,y=70)
    scr = Scrollbar(search_tap, orient=VERTICAL, command=search_result.yview)
    scr.grid(row=3, column=2, rowspan=15, columnspan=2, sticky=NS)
    search_result.grid(row=3, column=1, sticky=W)
    search_result.config(yscrollcommand=scr.set, font=('Arial', 8, 'bold', 'italic'))

    # lb = Listbox(fav_tap, name='lb')

    # search_result.pack()

    lb_f = Listbox(fav_tap,height=16,width=125)
    Label(fav_tap,text='Your FAV:').place(x=5,y=0)
    scr2 = Scrollbar(fav_tap, orient=VERTICAL, command=lb_f.yview)
    scr2.grid(row=3, column=1, sticky=NS,pady=(28,0))
    lb_f.grid(row=3, column=0, sticky=W,pady=(24,0),padx=(0,0))
    lb_f.config(yscrollcommand=scr2.set, font=('Arial', 10, 'bold'))

    num_f = None

    def open_link():
        global num_f
        global new_list
        global n_user
        if n_user:
            messagebox.showinfo(title='error', message=f'please choice product..')
        else:
            num_f = int(num_f) + len(last_list)
            webbrowser.open(new_list[num_f][2])

    def reCheak():
        global num_f
        global new_listview_my_fav
        global n_user
        if n_user:
            messagebox.showinfo(title='error', message=f'please choice product..')
        else:
            num_f = int(num_f) + len(last_list)
            if new_list[num_f][3] == 'e_bay':
                new_line = e_bay_price(new_list[num_f][2])
                # print(new_line, now)
            elif new_list[num_f][3] == 'walmart':
                new_line = wal_price(new_list[num_f][2])
            elif new_list[num_f][3] == 'newegg':
                new_line = newegg_price(new_list[num_f][2])
            elif new_list[num_f][3] == 'etsy':
                new_line = etsy_price(new_list[num_f][2])

            new_list[num_f][4], new_list[num_f][5] = new_line,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_2_DB()
            view_my_fav()

    def delete_fav():
        global user
        global num_f
        global n_user
        print(n_user)
        if n_user:
            messagebox.showinfo(title='error', message=f'please choice product..')
        else:
            del new_list[num_f+len(last_list)]

            save_2_DB()
            view_my_fav()

    def save_2_DB():
        global new_list
        global last_list

        with open('../../saves.csv', 'w', encoding="utf8", newline='') as writeFile:
            writer = csv.writer(writeFile)

            # writer.writerows(last_list)
            writer.writerows(new_list)

    b4 = Button(fav_tap,text='Delete',command=delete_fav, font=30).grid(row=4,column=0,pady=20,padx=(0,650))
    b5 = Button(fav_tap,text='re Check',command=reCheak, font=30).grid(row=4,column=0,pady=20,padx=(0,0))
    b6 = Button(fav_tap,text='Visit Link',command=open_link, font=30).grid(row=4,column=0,pady=20,padx=(650,0))


    def onselect2(evt):
        global num_f
        w = evt.widget
        value = int(w.curselection()[0])
        print('You selected item %d: ' % (value))
        # text2.insert(1, value)
        num_f = value
        # return value


    lb_f.bind('<<ListboxSelect>>', onselect2)



    def save_to():
        global newlist
        global user
        global choice
        print(choice)
        num = int(choice)

        messagebox.showinfo(title='Done', message=f'add')

        with open('../../saves.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows([[user, newlist[num - 1].title, newlist[num - 1].link,
            newlist[num - 1].website, newlist[num - 1].price, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]])

        view_my_fav()


    def sign_out():
        messagebox.showinfo(title='C U', message=f'Thank you for using our tool.. :)')
        window.destroy()
        while True:
            new_window()
            new_window2()


    b3 = Button(search_tap,text='Search',command=new_search, font=30).place(x=700, y=30)


    b2 = Button(text='Sign Out', bg='plum',command=sign_out, font=50).pack()



    def ittr():
        global minute
        global counter
        global timeer
        minuts = int(minute.get())

        if counter:
            if timeer >= minuts * 60000:
                timeer = 0
                auto(user)
                view_my_fav()
                window.after(1000, ittr)
            else:
                timeer += 1000
                label_6.config(text=f'Iteration time remaining: {(minuts * 60000 - timeer)//1000}')
                label_6.place(x=320, y=380)
                window.after(1000, ittr)

    def ittration():
        global event
        global minute
        global label_6
        global user_list
        global minute
        global counter
        minuts = int(minute.get())

        if len(user_list) == 0:
            messagebox.showinfo(title='erorr', message=f'please add some products to your favourite..')
        else:
            counter = True
            window.after(1000, ittr)
            messagebox.showinfo(title='Done', message=f'Iteration add')
            label_6.config(text=f'add new Iteration every: {minuts} minutes')
            label_6.place(x=320, y=380)



    def itt_stop():
        global counter
        global label_6
        counter = False
        messagebox.showinfo(title='Done', message=f'Iteration cancled')
        label_6.config(text=f'cancled last Iteration')
        label_6.place(x=320, y=380)

        # label_6 = Label(ittraion_tap, text=f'cancled last Iteration').place(x=325, y=380)


    label_0 =Label(ittraion_tap,text="Auto Update Prices",font=("bold",35)).place(x=230,y=70)
    label_1 =Label(ittraion_tap,text="Last check :", width=15,font=("bold",16))
    label_1.place(x=270,y=150)


    label_3 =Label(ittraion_tap,text="Check / Update each :", width=20,font=("bold",16))
    label_3.place(x=150,y=213)
    entry_3=Entry(ittraion_tap,textvariable=minute)
    entry_3.place(x=430,y=217)
    label_333 =Label(ittraion_tap,text="min", width=-8,font=("bold",12)).place(x=600,y=217)

    button1=Button(ittraion_tap,text='Start',font=("bold",12) ,command =ittration,relief=RAISED,cursor="hand2" ,width=20,height="3",bg="black",fg='white').place(x=180,y=290)
    button2=Button(ittraion_tap,text='Stop' ,font=("bold",12),relief=RAISED,cursor="hand2",command =itt_stop, width=20,height="3",bg="black",fg='white').place(x=550,y=290)

    #########################################

    Label(about_us_tap, text="About Us:",font='50').grid(row=0, column=0, pady=30)
    Label(about_us_tap, text="Machine_Teacherz",fg = "light green", bg = "dark green",font = "Helvetica 20 bold italic").place(x=310,y=40)

    def add_about(path,col):
        load = Image.open(path)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(about_us_tap,image=render)
        img.image = render
        img.grid(row=1, column=col, padx=10, pady=20)
        # img.pack()

    add_about('our_photos/1.jpg',0)
    add_about('our_photos/2.jpg',3)
    add_about('our_photos/3.png',2)
    add_about('our_photos/4.jpg',1)

    Label(about_us_tap, text="Mohammad Nemrawi",fg = "blue", bg = "yellow", font = "Verdana 10 bold").grid(row=2, column=0)
    Label(about_us_tap, text="Emad Al-Deen\nAlzoubi",fg = "blue", bg = "yellow", font = "Verdana 10 bold").grid(row=2, column=3)
    Label(about_us_tap, text="Majd Alkilany",fg = "blue", bg = "yellow", font = "Verdana 10 bold").grid(row=2, column=2)
    Label(about_us_tap, text="Osama Yousef",fg = "blue", bg = "yellow", font = "Verdana 10 bold").grid(row=2, column=1)

    Label(about_us_tap, text="Software Engineer\nI have good experience\nworking in frontend and backend",fg = "white", bg = "blue", font = "Verdana 10").grid(row=3, column=0, pady=10)
    Label(about_us_tap, text="software developer\nfreshly graduated from ASAC",fg = "white", bg = "blue", font = "Verdana 10").grid(row=3, column=1, pady=10)
    Label(about_us_tap, text="software developer\nfreshly graduated from ASAC",fg = "white", bg = "blue", font = "Verdana 10").grid(row=3, column=2, pady=10)
    Label(about_us_tap, text="software developer\nfreshly graduated from ASAC",fg = "white", bg = "blue", font = "Verdana 10").grid(row=3, column=3, pady=10)



    view_my_fav()

    window.mainloop()

# auto(user_list)
# schedule.run_pending()

new_window()
new_window2()

# if __name__ == '__main__':
    # time.sleep(5)
    # print('hii')

