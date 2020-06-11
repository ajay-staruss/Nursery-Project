from django.shortcuts import render,redirect
from .models import Cart,Checkout
from django.shortcuts import get_object_or_404
from seller.models import AddPlant

# Create your views here.

def add_to_cart(request, product_id):
	if request.user.is_authenticated:
		details = get_object_or_404(AddPlant, pk=product_id)
		pic = details.photo
		name = details.name
		price = details.price
		seller_us = details.u_name
		us = request.user.username
		cart = Cart(pic=pic,name=name,price=price,us=us,seller_us=seller_us)
		cart.save()
		return redirect('shop')
	else:
		return redirect('shop')
def cart(request):
	if request.user.is_authenticated:
		cart = Cart.objects.filter(us=request.user.username)
		total = 0
		for i in cart:
			total=total+i.price
			print(total)
		context = {
			'cart':cart,
			'total':total
		}
		return render(request,'cart.html',context)
	else:
		return redirect('index')

def checkout(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		phone = request.POST['phone']
		address = request.POST['address']
		town = request.POST['town']
		state = request.POST['state']
		country = request.POST['country']
		order_notes = request.POST['order_notes']
		use = request.user.username
		c = Cart.objects.filter(us=request.user.username)
		product_name =''
		for i in c:
			seller_use = i.seller_us
			product_name = product_name+', '+i.name
		checkout = Checkout(fname=fname,lname=lname,email=email,phone=phone,address=address,town=town,state=state,country=country,order_notes=order_notes,use=use,seller_use=seller_use,product_name=product_name)
		checkout.save()
		c = Cart.objects.filter(us=request.user.username)
		c.delete()
		return redirect('thankyou')
	else:
		c = Cart.objects.filter(us=request.user.username)
		total = 0
		for i in c:
			total+=i.price
		shipping = 50
		order_total = total+shipping
		context = {
			'cart':c,
			'total':total,
			'shipping':shipping,
			'order_total':order_total
		}
		return render(request,'checkout.html',context)


def thankyou(request):
	return render(request,'thankyou.html')