import os
import cv2 as cv
import numpy as np

people=[]
DIR=r'C:\Users\USER\OneDrive\Documents\VSCode\OpenCV\Resources\Faces\train'
for i in os.listdir(DIR):
    people.append(i)

# creating the model

haar_cascade= cv.CascadeClassifier(r'C:/Users/USER/OneDrive/Documents/VSCode/haar_face.xml')
features=[]
labels=[]

def create_train():
    for person in people:
        path= os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(gray,1.1,4)

            for (x,y,w,h) in face_rect:
                faces_roi=gray[y:y+h,x:x+w]

                features.append(faces_roi)
                labels.append(label)

create_train()

print(f'Number of features= {len(features)}')
print(f'Number of labels= {len(labels)}')

# Recognizer

features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

# Saving the model

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
