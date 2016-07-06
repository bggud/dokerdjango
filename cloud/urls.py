from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.cloud_view,name='cloud_view'),
]
