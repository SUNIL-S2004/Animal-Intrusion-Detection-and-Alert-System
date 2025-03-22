from ultralytics import YOLO
import pyrebase
import time

# Firebase configuration
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

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Load YOLO model
model = YOLO("D:/aidas/best.pt")
camera_source = "rtsp://192.168.159.102/live/ch00_0"

# Flag to control the loop
elephant_detected = False

# Stream the predictions
results = model.predict(source=0, stream=True, conf=0.7, show=True)

for result in results:
    # Check detections
    for box in result.boxes:
        class_id = int(box.cls)
        class_name = result.names[class_id]
        
        if class_name.lower() == "elephant":  # If elephant detected
            elephant_detected = True  # Stop the detection process
            
            # Send notification to Firebase
            deteco = {
                'Time': time.ctime(time.time()),
                'Message': "Elephant Detected"
            }
            
            try:
                db.child("notifications").push(deteco)
                print(f"Elephant detected and notification sent at {time.ctime(time.time())}.")
            except Exception as e:
                print("Failed to send notification:", e)
                
            break  # Break the loop when elephant is detected

    if elephant_detected:
        print("Elephant detected! Exiting the detection process.")
        break  # Stop the whole process