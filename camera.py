import cv2
import numpy as np

class vcam():
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self, level):
		ret, frame = self.video.read()
		width = frame.shape[0]
		height = frame.shape[1]
		fact = 1.4
		resized = cv2.resize(frame, (int(height/fact), int(width/fact)))

		img_width = resized.shape[0]
		img_height = resized.shape[1]
		
		#v = 0, normal
		if level == 0:
			ret, jpeg = cv2.imencode('.jpg', resized)

		#moving away, redshift
		elif level > 0:
			img = np.ones((img_width, img_height,3),np.uint8)
			width = img_width*2
			img[:,0:width] = (0,0,level)    
			final = cv2.add(resized, img)
			ret, jpeg = cv2.imencode('.jpg', final)

		#moving closer, blueshift
		elif level < 0:
			level = level*(-1)
			img = np.ones((img_width, img_height,3),np.uint8)
			width = img_width*2
			img[:,0:width] = (level,0,0)    
			final = cv2.add(resized, img)
			ret, jpeg = cv2.imencode('.jpg', final)

		return jpeg.tobytes()
