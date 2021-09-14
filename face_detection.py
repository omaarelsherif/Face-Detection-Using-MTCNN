### Face Detection ###
"""
Description:
			 Appply face detection using Multi-Task Cascaded Convolutional Neural Network model "MTCNN" 
Paper :
		https://arxiv.org/abs/1604.02878
"""

# 1 | Import modules
import sys
import cv2
from mtcnn.mtcnn import MTCNN

# 2 | Load the image by the path from cmd
path = sys.argv
img = cv2.imread(path[1])

# 3 | Create an object of MTCNN detector
detector = MTCNN()
 
# 4 | Detect faces in the image
faces = detector.detect_faces(img)

# 5 | Draw dtected faces on the images
def draw_faces(img, faces_list):
	"""Function to draw the bounding boxs of detected faces in an image"""
	for face in faces_list:
		# Get bounding box coordinates
		x, y, width, height = face['box']
		cord_x = x + width
		cord_y = y + height
		# Draw a rectangle 
		rect = cv2.rectangle(img, (x,y), (cord_x,cord_y), (0,255,0), 4)
	# Show the image 
	cv2.imshow("Face Detection", img)
	cv2.waitKey(0)

# 6 | Display faces on the original image
draw_faces(img, faces)
