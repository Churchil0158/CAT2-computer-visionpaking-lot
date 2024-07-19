# Import necessary libraries
import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('C:/Users/LENOVO YOGA 11E/Downloads/parking_lot_video.mp4')

# Define the list of parking space coordinates (x, y, width, height)
# Adjust these coordinates based on your specific parking lot
parking_spaces = [
    (100, 200, 50, 100),
    (200, 200, 50, 100),
    # Add more parking spaces as needed
]

# Function to check if a parking space is occupied
def is_occupied(space, frame):
    x, y, w, h = space
    roi = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)[1]
    count = cv2.countNonZero(thresh)
    return count > (w * h * 0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    for space in parking_spaces:
        x, y, w, h = space
        if is_occupied(space, frame):
            color = (0, 0, 255)  # Red for occupied
            label = "Occupied"
        else:
            color = (0, 255, 0)  # Green for empty
            label = "Empty"
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    cv2.imshow('Parking Occupancy Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
