
import cv2
import numpy as np

# Start capturing video
cap = cv2.VideoCapture(0)

# Allow the camera to warm up and capture the background
print("Capturing background. Please stay out of the frame.")
for i in range(50):  # Capture multiple frames to stabilize background
    ret, background = cap.read()
background = cv2.flip(background, 1)  # Flip the background for a mirror-like effect
print("Background captured. You can step into the frame now!")

# Define HSV range for black
lower_black = np.array([0, 0, 0])  # Adjust for pure black
upper_black = np.array([180, 255, 80])  # Adjust to include brighter edges

# Start reading frames from the webcam
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for consistency
    frame = cv2.flip(frame, 1)

    # Smooth the frame to reduce noise and edge artifacts
    blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0)

    # Convert the blurred frame to HSV color space
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the black cloak
    cloak_mask = cv2.inRange(hsv, lower_black, upper_black)

    # Refine the mask (reduce noise and clean edges)
    cloak_mask = cv2.morphologyEx(cloak_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    cloak_mask = cv2.morphologyEx(cloak_mask, cv2.MORPH_DILATE, np.ones((7, 7), np.uint8))

    # Create an inverted mask for the non-cloak region
    non_cloak_mask = cv2.bitwise_not(cloak_mask)

    # Segment out the cloak region and replace it with the background
    cloak_region = cv2.bitwise_and(background, background, mask=cloak_mask)
    non_cloak_region = cv2.bitwise_and(frame, frame, mask=non_cloak_mask)
    combined = cv2.addWeighted(cloak_region, 1, non_cloak_region, 1, 0)

    # Display the final output
    cv2.imshow('Invisibility Cloak', combined)

    # Debug: Display the mask to verify it
    cv2.imshow('Cloak Mask', cloak_mask)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
