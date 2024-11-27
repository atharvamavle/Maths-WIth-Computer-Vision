# We have installed cvzone (is help to run code in more easier way) , mediapipe (for Tracking)

import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image('file.png')

col1 , col2 = st.columns([2,1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    output_text_area = st.title('Answer')
    output_text_area = st.subheader("")

genai.configure(api_key='AIzaSyCFLYVOJv-Wt2UYofgwYCuY25NhomlRPbU')
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(propId=3,value=1280) #Width
cap.set(propId=4,value=780) #Height

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)


def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
       

        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers , lmList
    else:
        return None
    

# We are writing code to draw the objects on the canva using our hand gesture
def draw (info, prev_pos, canvas):  
    fingers , lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos= lmList [8][0:2]

        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas , current_pos, prev_pos, color=(255, 0, 127), thickness=10)

    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros(img.shape, dtype=np.uint8)

    return current_pos , canvas



def sendToAI(model, canvas , fingers):
    if fingers == [1,1,1,1,0] :
        pil_image= Image.fromarray(canvas)

        
        # Construct a prompt based on the finger gesture
        prompt = "Solve the mathematical equation depicted in the image."

        response = model.generate_content([prompt, pil_image])
        return response.text

prev_pos = None
image_combine = None
canvas = None
output_text= ""

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img = cv2.flip(img , flipCode= 1)

    
    # Creating Canvas
    if canvas is None:
        canvas = np.zeros(img.shape, dtype=np.uint8)
        


    info = getHandInfo(img)
    if info:
        fingers , lmList = info #unzipping this list we are gtting value
       
        prev_pos_canvas= draw (info , prev_pos , canvas)
        output_text=sendToAI(model,canvas,fingers)



    image_combine = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combine,channels='BGR')
    output_text_area.text(output_text)


       

    # Display the image in a window
    # cv2.imshow("Image", img)
    # cv2.imshow("Canavas", canvas)
    # cv2.imshow("image_combine", image_combine)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)