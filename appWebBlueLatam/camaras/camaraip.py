import cv2

class LiveWebCam():
	def __init__(self):
		self.url = cv2.VideoCapture('rtsp://admin:IP80IV@201.218.147.13/1')

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()


		