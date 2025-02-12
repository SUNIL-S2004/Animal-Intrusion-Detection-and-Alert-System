# from ultralytics import YOLO
# import numpy
# import cv2

# model = YOLO("D:/aidas/best.pt")
# model.predict(source="0", show = True, conf = 0.7 )
#***************************************************************************************
# import pyrebase

# firebaseConfig={
#     'apiKey': "AIzaSyAaYhwQ5OhDRBEQVyy5D55g9hUnoiqBOr4",
#     'authDomain': "aidas-web.firebaseapp.com",
#     'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
#     'projectId': "aidas-web",
#     'storageBucket': "aidas-web.appspot.com",
#     'messagingSenderId': "54804411221",
#     'appId': "1:54804411221:web:4874ebc2305823128d75dc",
#     'measurementId': "G-FK2YR4248E"}

# firebase=pyrebase.initialize_app(firebaseConfig)

# db=firebase.database()
# storage=firebase.storage()
# name=input("enter the name")


# data={"name":name}
# db.child("user").push(data)
#*****************************************************************************************

# from ultralytics import YOLO
# import numpy as np
# import cv2
# import pyrebase

# # # Initialize YOLO model
# model = YOLO("D:/aidas/best.pt")

# # # Predict using YOLO model
# predictions = model.predict(source="0", conf=0.7)

# # # Initialize Firebase
# firebaseConfig = {
#     'apiKey': "YOUR_API_KEY",            
#     'authDomain': "aidas-web.firebaseapp.com",
#     'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
#     'projectId': "aidas-web",
#     'storageBucket': "aidas-web.appspot.com",
#     'messagingSenderId': "54804411221",
#     'appId': "1:54804411221:web:4874ebc2305823128d75dc",
#     'measurementId': "G-FK2YR4248E"}

# firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()


# db.child("predictions").push(predictions)

# Input name
# name = input("Enter the name: ")

# # Save name to Firebase
# data = {"name": name}
# db.child("user").push(data)

# You can save predictions to Firebase as well if needed
# Assuming predictions is a list of predictions
# You need to convert the predictions to a format suitable for Firebase
# For example, converting them to a dictionary
# Then, you can push this data to Firebase

# For example, if predictions is a list of dictionaries
# You can directly push it to Firebase


# If predictions is a numpy array or any other format,
# you need to convert it to a suitable format before pushing to Firebase

# Example:
# Convert predictions to a dictionary
# predictions_dict = predictions.tolist()  # Assuming predictions is a numpy array
# db.child("predictions").push(predictions_dict)

#******************************************************************************************************************
# try:
#     from ultralytics import YOLO
#     import numpy as np
#     import cv2
#     import pyrebase

#     # Initialize YOLO model
#     model = YOLO("D:/aidas/best.pt")

#     # Predict using YOLO model
#     predictions = model.predict(source="0", conf=0.7)

#     # Initialize Firebase
#     firebaseConfig = {
#         'apiKey': "YOUR_API_KEY",            
#         'authDomain': "aidas-web.firebaseapp.com",
#         'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
#         'projectId': "aidas-web",
#         'storageBucket': "aidas-web.appspot.com",
#         'messagingSenderId': "54804411221",
#         'appId': "1:54804411221:web:4874ebc2305823128d75dc",
#         'measurementId': "G-FK2YR4248E"
#     }

#     firebase = pyrebase.initialize_app(firebaseConfig)
#     db = firebase.database()

#     # Convert predictions to a dictionary
#     predictions_dict = {
#         "labels": predictions.xyxy[0][:, -1].tolist(),  # Extract labels
#         "boxes": predictions.xyxy[0][:, :-1].tolist()  # Extract bounding boxes
#     }

#     # Push predictions to Firebase
#     db.child("predictions").push(predictions_dict)

#     print("Predictions pushed to Firebase successfully!")

# except KeyboardInterrupt:
#     print("Execution interrupted. Exiting...")
#***************************
'''try:

    from ultralytics import YOLO
    model = YOLO("D:/aidas/best.pt")
    model.predict(source="0", show = True, conf = 0.7 )
except KeyboardInterrupt:
    import pyrebase
    firebaseConfig = {
        'apiKey': "YOUR_API_KEY",            
        'authDomain': "aidas-web.firebaseapp.com",
        'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
        'projectId': "aidas-web",
        'storageBucket': "aidas-web.appspot.com",
        'messagingSenderId': "54804411221",
        'appId': "1:54804411221:web:4874ebc2305823128d75dc",
        'measurementId': "G-FK2YR4248E"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    db.child("notifications").push({"message":"animal detected"})
    print("animal detected")
    '''
#***********************************************
# from ultralytics import YOLO

# try:
#     model = YOLO("D:/aidas/best.pt")
#     output = model.predict(source="0", show=True, conf=0.7)
#     detections = len(output.pred)
#     print("Total number of detections:", detections)
# except KeyboardInterrupt:
#     import pyrebase
#     import time
#     firebaseConfig = {
#         'apiKey': "YOUR_API_KEY",            
#         'authDomain': "aidas-web.firebaseapp.com",
#         'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
#         'projectId': "aidas-web",
#         'storageBucket': "aidas-web.appspot.com",
#         'messagingSenderId': "54804411221",
#         'appId': "1:54804411221:web:4874ebc2305823128d75dc",
#         'measurementId': "G-FK2YR4248E"
#     }
#     firebase = pyrebase.initialize_app(firebaseConfig)
#     db = firebase.database()
#     deteco = {
#         'Time':time.time(),
#         'Message':"Elephant Detected",

#     }
#     db.child("notifications").push(deteco)
#     print("animal detected")

#***********************************************
from ultralytics import YOLO
import re

try:
    model = YOLO("D:/aidas/best.pt")
    camera_source = 0
    output = model.predict(source=camera_source, show=True, conf=0.7)
    detections = len(output.pred)

    # Count the occurrences of 'Elephant' (case insensitive) in the output
    count_elephants = len(re.findall(r'elephant', output.names, re.IGNORECASE))

    print("Total number of detections:", detections)
    print("Total number of Elephants detected:", count_elephants)
except KeyboardInterrupt:
    import pyrebase
    import time

    firebaseConfig = {
        'apiKey': "YOUR_API_KEY",            
        'authDomain': "aidas-web.firebaseapp.com",
        'databaseURL': "https://aidas-web-default-rtdb.asia-southeast1.firebasedatabase.app/",
        'projectId': "aidas-web",
        'storageBucket': "aidas-web.appspot.com",
        'messagingSenderId': "54804411221",
        'appId': "1:54804411221:web:4874ebc2305823128d75dc",  
        'measurementId': "G-FK2YR4248E"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    deteco = {
        'Time': time.ctime(time.time()),
        'Message': "Elephant Detected",
        
    }
    db.child("notifications").push(deteco)
    

''' # Print the counts before exiting the program
    print("\nProgram terminated by user.")
    print("Total number of detections:", detections)
    print("Total number of Elephants detected:", count_elephants)'''


# "now < 1710700200000"
# "now < 1710700200000"