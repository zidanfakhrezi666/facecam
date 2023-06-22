#!/usr/bin/env python
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
face_cascade = cv2.CascadeClassifier("/home/jetson2gb/cascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/jetson2gb/cascade/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
while 1: 
     
        pub = rospy.Publisher("frames", Image, queue_size=2)
        rospy.init_node('stream_publisher', anonymous=True)
        rate = rospy.Rate(10)

	ret, img = cap.read() 


	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		 
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		
		eyes = eye_cascade.detectMultiScale(roi_gray) 

		
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

	
	cv2.imshow('img',img)
        
        bridge= CvBridge() 
            
        ros_image = bridge.cv2_to_imgmsg(img, "bgr8")
        pub.publish(ros_image)
        rate.sleep()

	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break


cap.release()


cv2.destroyAllWindows() 
