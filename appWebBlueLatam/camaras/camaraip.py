from django.db import IntegrityError
from camaras.models import (
	Resultado,
	Camara
)
import cv2
import requests
import json
import datetime

class LiveWebCam():
	def __init__(self, request, camara):
		self.request = request
		self.camara = camara
		self.url = cv2.VideoCapture(camara.ip) #rtsp://ad min:IPBOIV@192.168.20.107/h264_stream

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()

		"""try:
			# URL for the web service
			scoring_uri = '<your web service URI>'
			# If the service is authenticated, set the key or token
			key = '<your key or token>'

			# Set the content type
			headers = {'Content-Type': 'application/json'}
			# If authentication is enabled, set the authorization header
			headers['Authorization'] = f'Bearer {key}'

			# Postear el request
			resp = requests.post(scoring_uri, imgNp, headers=headers)
			
			# Ingresar aqui a la base de datos el json

			try:
				resultado = Resultado.objects.create(
					resultado_json=resp,
					fecha=datetime.datetime.now(),
					camara=self.camara
					)
				
				resultado.save()

			except IntegrityError as ie:
				print(ie)

		except Error as e:
			print(e)"""

		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)

		return jpeg.tobytes()