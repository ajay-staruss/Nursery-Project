from django.shortcuts import render,redirect
from .models import AddPlant
from django.shortcuts import get_object_or_404
from buyer.models import Checkout
# Create your views here.
def plant(request):
	if request.method == 'POST':
		name = request.POST['name']
		price = request.POST['price']
		description = request.POST['description']
		image = request.FILES['image']
		u_name = request.user.username
		addplant = AddPlant(name=name,price=price,description=description,photo=image,u_name=u_name)
		addplant.save()
		return redirect('addPlant')
	else:
		if(request.user.profile.usertype == 'seller'):
			return render(request,'seller.html')
		else:
			return redirect('index')

def shop(request):
	addplant = AddPlant.objects.all()
	context = {
		'addplant':addplant
	}
	return render(request,'shop.html',context)

def shopdetails(request, shop_id):
	details = get_object_or_404(AddPlant,pk=shop_id)
	context = {
		'details':details,
		'product_id':shop_id
	}
	return render(request,'shop-details.html',context)

def sellerdashboard(request):
	checkout = Checkout.objects.filter(seller_use=request.user.username)
	context = {
		'checkout':checkout
	}
	return render(request,'sellerdashboard.html',context)