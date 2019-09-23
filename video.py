import cv2
import os
import numpy as np
import faceRecognition as fr
import datetime
import winsound


##for(x,y,w,h) in faces_detected:
##	cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)
##
##resized_img = cv2.resize(test_img,(400,500))	
##cv2.imshow("face detection",resized_img)
##cv2.waitKey(0)
##cv2.destroyAllWindows

def main():
      
##        faces,faceID = fr.labels_for_training_data("training")
##        face_recognizer = fr.train_classifier(faces,faceID)
##        face_recognizer.save("trainingData.yml")

        face_recognizer=cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read("trainingData.yml")

       



        name = {0:"Fariha",1:"Inara",2:"Arowa",3:"Ankon",4:"Farhan",5:"Minhaz",6:"Afifa",7:"Karishma",8:"Nafisa"}
        gender = {0:"Female",1:"Male",2:"Female",3:"Male",4:"Male",5:"Male",6:"Female",7:"Female",8:"Female"}
        relation = {0:"Sister",1:"Cousin",2:"Aunt",3:"Uncle",4:"Nephew",5:"Child",6:"Enemy",7:"Mother",8:"Daughter"}
        prof = {0:"Student",1:"MUA",2:"Student",3:"Student",4:"Student",5:"Student",6:"Villain",7:"Student",8:"Student"}
       
                   

        cap=cv2.VideoCapture(0)

        while True:
                ret,test_img=cap.read()
                faces_detected,gray_img = fr.faceDetection(test_img)


                for face in faces_detected:
                        (x,y,w,h) = face
                        roi_gray = gray_img[y:y+h,x:x+h]
                        label,confidence = face_recognizer.predict(roi_gray)
                        print("confidence:",confidence)
                        print("label:",label)
                        fr.draw_rect(test_img,face)
                        predicted_name = name[label]
                        predicted_relation = relation[label]
                        predicted_prof = prof[label]
                      
                        if(confidence<50):
                                if(cv2.waitKey(1)==ord('s')):
                                        if (label==0):
                                                winsound.PlaySound("Fariha.wav",winsound.SND_ASYNC)
                                        elif (label == 1):
                                                winsound.PlaySound("Inara.wav",winsound.SND_ASYNC)
                                        elif (label == 2):
                                                winsound.PlaySound("Arowa.wav",winsound.SND_ASYNC)
                                        elif (label == 3):
                                                winsound.PlaySound("Ankon.wav",winsound.SND_ASYNC)
                                        elif (label == 4):
                                                winsound.PlaySound("Farhan.wav",winsound.SND_ASYNC)
                                        elif (label == 5):
                                                winsound.PlaySound("Minhaz.wav",winsound.SND_ASYNC)
                                        elif (label == 6):
                                                winsound.PlaySound("Afifa.wav",winsound.SND_ASYNC)
                                        elif (label == 7):
                                                winsound.PlaySound("Karishma.wav",winsound.SND_ASYNC)
                                        elif (label == 8):
                                                winsound.PlaySound("Nafisa.wav",winsound.SND_ASYNC)        
                                
                                fr.put_text(test_img,predicted_name,x,y)
                                fr.put_text2(test_img,predicted_relation,x,y)
                                fr.put_text2(test_img,predicted_prof,x,y+h-50)
                                
                                if(gender[label]=="Female"):
                                     s_img = cv2.imread("pin2.png")
                                elif(gender[label]=="Male"):
                                     s_img = cv2.imread("pin3.png")
                                r_img = cv2.imread("relation.png")
                                p_img = cv2.imread("prof.png") 
                                x_offset=x
                                y_offset=y-50
                                test_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
                                x1 = x+10
                                y1 = y +10
                                test_img[y1:y1 +r_img.shape[0], x1:x1+r_img.shape[1]] = r_img
                                x1 = x+10
                                y1 = y + h -40
                                test_img[y1:y1 +p_img.shape[0], x1:x1+p_img.shape[1]] = p_img

                              

                
                resized_img = cv2.resize(test_img,(1000,700))	
                cv2.imshow("face detection",resized_img)
                if cv2.waitKey(1) == ord('q'):
                        break
                
        
        cap.release()        
        cv2.destroyAllWindows
