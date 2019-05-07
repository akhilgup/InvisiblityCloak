import numpy as np
import cv2
import time

#Reading the webcam

cap = cv2.VideoCapture(0)

time.sleep(3)
count = 0
background = 0

#Capturing the background in range of 50

for i in range(50):
	ret, background = cap.read()
background = np.flip(background, axis = -1)
print ("tru")
#When the webcam is openend, are readingthe images from the webcam

while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
		break
	count += 1
	img =np.flip(img, axis = 1)

	#Converting the color space from BGR to HSV

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	#Generating mask to detect color

	# Range for lower red
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)
	 
	# Range for upper range
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask1 = mask1 + mask2

	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	#Generating the final output

	res1 = cv2.bitwise_and(background,background,mask=mask1)
	res2 = cv2.bitwise_and(img,img,mask=mask2)
	final_output = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow("OUTPUT",final_output)
	k = cv2.waitKey(10)
	if k == 27:
	    break

