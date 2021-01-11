import cv2

class LiveWebCam():
	def __init__(self):
		self.url = cv2.VideoCapture('rtsp://admin:IPBOIV@192.168.20.107/h264_stream')

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()


		