from django.conf.urls import url, re_path
from django.urls import path, include
from camaras import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]