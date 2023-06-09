import cv2
window_title = "Face Detect"

face_cascade = cv2.CascadeClassifier("/home/jetson2gb/cascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/jetson2gb/cascade/haarcascade_eye.xml")

cam = cv2.VideoCapture(0)
cam.set(3, 320)
cam.set(4, 240)
flip=2

while True:
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0),2)
		roi_gray = gray[y : y + h, x : x + w]
		roi_color = frame[y : y + h, x : x + w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
 
	cv2.imshow("raimu", frame)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
