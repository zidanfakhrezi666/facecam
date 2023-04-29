import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 320)
cam.set(4, 240)
flip=2
while True:
	ret, frame = cam.read()
	cv2.imshow("raimu", frame)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()