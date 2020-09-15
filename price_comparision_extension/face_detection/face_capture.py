import cv2 
import numpy as np 
import face_recognition  
import os




def capture_img () : 
    your_name = input('input your name >>   ').upper()
    print ( 'press s to take photo ')
    print ( 'press q to quiet ')
    cam = cv2.VideoCapture(0)   
    while True :
        s, img = cam.read()
        cv2.imshow('webcam',img)
        key = cv2.waitKey(1)
        if key == ord('s') :
            if s:    
                cv2.namedWindow("cam-test")
                cv2.waitKey(0)
                cv2.destroyWindow("cam-test")
                cv2.imwrite(f"price_comparision_extension/face_detection/photos/{your_name}.jpg",img)

                return img
        if key == ord('q') :
            break



        




def lists_img() :
    path = 'price_comparision_extension/face_detection/photos'

    images = []

    photos_names = []

    mylist = os.listdir(path)
    # print(mylist)

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



def check_img() :
    images ,photos_names = lists_img()
    x= None
    img = capture_img()
    encode_list = find_encodings(images)
    if len(face_recognition.face_encodings(img))  > 0 : 


        encode_one = face_recognition.face_encodings(img)[0]
        for encode_img in encode_list : 
            results = face_recognition.compare_faces([encode_one],encode_img)
            if results[0] == True : 
                x = True
            else :
               x =  False
    else : 
           print("No faces found in the image!")


    if x == True :
        try: 
            os.remove(img)
        except: pass

    return x
    


if __name__ == "__main__":







    print(check_img())
    # print(capture_img())