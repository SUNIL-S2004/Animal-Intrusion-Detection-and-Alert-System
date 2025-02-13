# from ultralytics import YOLO
# model = YOLO("C:/Users/sande/Documents/College/Sem 4/Animal/yolov8n.pt")
# model.predict(source="0", save=True, show=True, conf=0.7, save_txt=True)


from ultralytics import YOLO
from twilio.rest import Client
import time

# --- Twilio SMS Setup ---
def send_sms_alert_twilio():
    account_sid = 'your_private_key'
    auth_token = 'your_private_key'
    client = Client(account_sid, auth_token)

    from_number = '+18285229174'  # Your Twilio phone number
    to_number = '+919361028156'   # Recipient phone number
    message_body = "Alert: Elephant detected at 17.4255716, 78.6455365 "

    try:
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        print("SMS sent successfully! Message SID:", message.sid)
    except Exception as e:
        print("Error sending SMS:", e)

# --- YOLOv8 Detection Setup ---
model = YOLO("C:/Users/sande/Documents/College/Sem 4/Animal/best.pt")

ELEPHANT_THRESHOLD = 10
detection_count = 0  # Track the number of detections

print("Starting detection... (Press Ctrl+C to stop)")

try:
    while detection_count < ELEPHANT_THRESHOLD:
        results = model.predict(source="0", conf=0.7, show=True, verbose=False, stream=True)

        for result in results:
            if not result.boxes:  # Ensure there are detections
                continue

            for box in result.boxes:
                cls_id = int(box.cls[0].item())  # Extract class ID correctly
                class_name = model.names.get(cls_id, "").lower()

                if class_name == "elephant":
                    detection_count += 1
                    print(f"Elephant detected! Count: {detection_count}")

                    if detection_count >= ELEPHANT_THRESHOLD:
                        print("Threshold reached. Sending SMS alert...")
                        send_sms_alert_twilio()
                        print("Stopping detection.")
                        exit()  # Stop the program after sending SMS

        time.sleep(0.1)
    
except KeyboardInterrupt:
    print("\nDetection stopped by user.")
    print(f"Final overall elephant detection count: {detection_count}")
