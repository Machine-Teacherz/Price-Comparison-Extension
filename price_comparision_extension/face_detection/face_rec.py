import cv2 
import numpy as np 
import face_recognition  
import os






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
# print(images,photos_names)

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

def find_face () :
    cap = cv2.VideoCapture(0)
    images , photos_names = lists_img()
    encode_lest_known = find_encodings(images)
    
    while True :
        success , img = cap.read()
        img_small =cv2.resize(img,(0,0),None,0.25,0.25)
        img_small = cv2.cvtColor(img_small,cv2.COLOR_BGR2RGB)
        faces_curr_frame = face_recognition.face_locations(img_small)
        encod_curr_frame = face_recognition.face_encodings(img_small,faces_curr_frame)

        for encode_face , face_loc in zip(encod_curr_frame , faces_curr_frame) :
            matches = face_recognition.compare_faces(encode_lest_known,encode_face)
            face_distance  = face_recognition.face_distance(encode_lest_known,encode_face)
            matche_index = np.argmin(face_distance)

            if matches[matche_index] : 
                name = photos_names[matche_index].upper()
                y1,x2,y2,x1 = face_loc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                return name
                
            else : 

                y1,x2,y2,x1 = face_loc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,'none',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                return 'None'



        cv2.imshow('webcam',img)
        key = cv2.waitKey(2)

        if key == ord('q') :
            break

if __name__ == "__main__":
    print(find_face () )