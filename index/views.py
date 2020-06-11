from django.shortcuts import render
from seller.models import AddPlant
# Create your views here.
def index(request):
	plant = AddPlant.objects.all()
	context = {
		'plant':plant
	}
	return render(request,'index.html',context)
def about(request):
	return render(request,'about.html')