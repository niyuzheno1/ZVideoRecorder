# importing the required packages 
import pyautogui 
import cv2 
import numpy as np 
import time
#get the first device
cap = cv2.VideoCapture(0)

def gethwc(frame):
    return np.array(frame).shape

# return (height, width, channel) for the screenshot
def get_height_width_channel():
    # Take screenshot using PyAutoGUI 
    img = pyautogui.screenshot() 
    # Convert the screenshot to a numpy array 
    frame = np.array(img) 
    # Convert it from BGR(Blue, Green, Red) to 
    # RGB(Red, Green, Blue) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    # Write it to the output file 
    #out.write(frame) 
    image_list.append(frame)  
    return gethwc(frame)

# Specify resolution 
resolution = (1920, 1080) 
  
# Specify video codec 
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  
  
# Specify name of Output file 
filename = "Recording.mp4"
  
# Specify frames rate. We can choose any  
# value and experiment with it 
fps = 12.0
  
  
# Creating a VideoWriter object 
  
# Create an Empty window 
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 
  
# Resize this window 
cv2.resizeWindow("Live", 480, 270) 

image_list = []

height,width,channel = get_height_width_channel()

resolution = (width, height) 

out = cv2.VideoWriter(filename, codec, fps, resolution) 


while cap.isOpened():
    # Take screenshot using PyAutoGUI 
    st = time.time()  # collect start time

    img = pyautogui.screenshot() 
    ret, camframe = cap.read()

    # Convert the screenshot to a numpy array 
    frame = np.array(img) 
    scale_percent = 30 # percent of original size
    wi = int(camframe.shape[1] * scale_percent / 100)
    he = int(camframe.shape[0] * scale_percent / 100)
    camframe = cv2.resize(camframe, (wi, he))
    # Convert it from BGR(Blue, Green, Red) to 
    # RGB(Red, Green, Blue) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    ch, cw, cc = gethwc(camframe)
    x_offset, y_offset = 0, 0
    frame[y_offset:y_offset+camframe.shape[0], x_offset:x_offset+camframe.shape[1]] = camframe
    
    #cv2.rectangle(frame, (0, 0), (cw, ch),
	#	(0, 0, 255), -1)
    # Write it to the output file 
    out.write(frame)   
    # Optional: Display the recording screen 
    cv2.imshow('Live', frame)  
    en = time.time()  # collect end time
    delay = max(0, (1 / fps - (en - st)) * 1000)  

    # Stop recording when we press 'q' 
    if cv2.waitKey(1) == ord('q'): 
        break



# Release the Video writer 
out.release() 
  
# Destroy all windows 
cv2.destroyAllWindows()