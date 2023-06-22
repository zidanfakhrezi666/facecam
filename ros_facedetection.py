#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

# Fungsi callback untuk menerima gambar dari topik /camera/image
def image_callback(msg):
    # Konversi gambar dari ROS Image menjadi OpenCV format
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")

    # Deteksi wajah menggunakan OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

    # Gambar kotak pada wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(cv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Menampilkan gambar dengan wajah yang terdeteksi
    cv2.imshow("Face Detection", cv_image)
    cv2.waitKey(1)

# Inisialisasi node ROS
rospy.init_node("face_detection_node")

# Membuat objek CvBridge
bridge = CvBridge()

# Membuat subscriber untuk topik gambar /camera/image
image_sub = rospy.Subscriber("/camera/image", Image, image_callback)

# Menampilkan informasi bahwa node siap
rospy.loginfo("Face detection node is ready")

# Menjalankan node ROS
rospy.spin()
