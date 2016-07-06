from django.shortcuts import render
from .models import Docker
# Create your views here.
def cloud_view(request):
	dkr = Docker.objects.filter()
	return render(request,'cloud/cloudIndex.html',{'dkr':dkr})
