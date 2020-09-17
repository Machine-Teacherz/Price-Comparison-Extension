import cv2
import numpy as np
import face_recognition
import os
from tkinter.simpledialog import askstring
from tkinter import messagebox
from tkinter.messagebox import showinfo
from datetime import datetime

def lists_img() :
    path = 'face_detection/photos'
    images = []
    photos_names = []
    mylist = os.listdir(path)
    for ph in mylist :
        cur_img = cv2.imread(f'{path}/{ph}')
        images.append(cur_img)
        photos_names.append(ph.split('.')[0])
    return images , photos_names
images ,photos_names = lists_img()
def capture_img () :
    your_name = askstring('Name', 'What is your name?').upper()
    now = datetime.now().second
    while your_name in  photos_names :
        your_name = input('this name already taken please coose another one   >>   ').upper()
    print ( 'press s to take photo ')
    print ( 'press q to quiet ')
    cam = cv2.VideoCapture(0)
    img = None
    while True :
        s, img = cam.read()
        cv2.imshow('webcam',img)
        key = cv2.waitKey(1)

        if datetime.now().second == now + 5:
            cv2.namedWindow("webcam")
            cv2.destroyWindow("webcam")
            cv2.imwrite(f"face_detection/photos/{your_name}.jpg", img)
            break
        # if key == ord('s') :
        #     if s:
        #         cv2.namedWindow("cam-test")
        #         cv2.waitKey(0)
        #         cv2.destroyWindow("cam-test")
        #         cv2.imwrite(f"face_detection/photos/{your_name}.jpg",img)
        # if key == ord('q') :
        #     cv2.destroyWindow("cam-test")
        #     break
    # x= None
    # encode_list = find_encodings(images)
    # if len(face_recognition.face_encodings(img))  > 0 :
    #     encode_one = face_recognition.face_encodings(img)[0]
    #     for encode_img in encode_list :
    #         results = face_recognition.compare_faces([encode_one],encode_img)
    #         if results[0] == True :
    #             x = True
    #         else :
    #            x =  False
    # else :
    #        print("No faces found in the image!")
    # if x == True :
    #         # os.remove(f"price_comparision_extension/face_detection/photos/{your_name}.jpg")
    #         pass
    return your_name

def lists_img() :
    path = 'face_detection/photos'
    images = []
    photos_names = []
    mylist = os.listdir(path)
    for ph in mylist :
        cur_img = cv2.imread(f'{path}/{ph}')
        images.append(cur_img)
        photos_names.append(ph.split('.')[0])
    return images , photos_names
images ,photos_names = lists_img()
# print(photos_names)
def find_encodings(imgs) :
    encode_list = []
    for img in imgs :
        if len(face_recognition.face_encodings(img))  > 0 :
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encode_list.append(encode)
        else :
            continue
    return encode_list
if __name__ == "__main__":
    capture_img ()