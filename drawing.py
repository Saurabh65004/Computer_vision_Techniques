import numpy as np
import cv2


###################
#Function##
###################
# Create a function based on a CV2 Event (Left button click)
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img,(x,y),100,(0,255,0),-1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_img,(x,y),100,(255,255,0),-1)
    
# This names the window so we can reference it      
cv2.namedWindow('my_drawing')
# Connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing',draw_circle)

###################
#displaying image##
###################

blank_img=np.zeros(shape=(512,512,3),dtype=np.int8)

#img=cv2.imread("testingPuppy.jpg")


while True:
    
    cv2.imshow("my_drawing",blank_img)
    
    if(cv2.waitKey(20) & 0xFF == 27):
        break;
    
cv2.destroyAllWindows()