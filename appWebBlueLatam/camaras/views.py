from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import StreamingHttpResponse
from camaras.camaraip import LiveWebCam
from camaras.models import KPI



# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def KPIView(request):
	data = {}

	kpi = KPI.objects.all()
	resultados = Resultado.objects.all()

	cont_con_casco = 0
	cont_con_chaleco = 0
	cont_total_casco = 0
	cont_total_chaleco = 0

	for i in resultados: #suposicion
		for j in i.resultado_json["pred_classes"]:
			if j == 1 and j == 2:
				cont_total_casco += 1
				if j == 1:
					cont_con_casco += 1
			elif j == 3 and j == 4:
				cont_total_chaleco += 1
				if j == 3:
					cont_con_chaleco += 1

	for i in kpi:
		if i.nombre_kpi == "Porcentaje uso casco":
			kpi.objects.get(nombre_kpi=i.nombre_kpi).update(kpi=cont_con_casco/cont_total_casco)
		if i.nombre_kpi == "Porcentaje uso chaleco":
			kpi.objects.get(nombre_kpi=i.nombre_kpi).update(kpi=cont_con_chaleco/cont_total_chaleco)

	data["kpi"] = KPI.objects.all()

	return (request, 'kpi.html', data)


def livecam_feed(request):
	camara = Camara.objects.get(usuario_fk=request.user)

	return StreamingHttpResponse(gen(LiveWebCam(request, camara)),
					content_type='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')                            