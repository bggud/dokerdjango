from django.shortcuts import render

# Create your views here.
def cloud_view(request):
	return render(request,'cloud/cloudIndex.html',{})
