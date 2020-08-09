import cv2
#lets define the function for mouse event
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:#this is the event for left click of mouse
      print(x,',',y)#it will print the x,y coordinates
      strxy=str(x)+','+str(y)
      cv2.putText(img, strxy, (x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
      cv2.imshow("image",img)
img=cv2.imread('village.png')
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)#it is a callback function that call the mouse event function
cv2.waitKey(0)
cv2.destroyAllWindows()
