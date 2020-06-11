"""NurseryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from index import views
from account import views as v
from seller import views as w
from buyer import views as b

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('register/',v.registration, name='register'),
    path('login/',v.login,name='login'),
    path('logout/',v.logout,name='logout'),
    path('addplant/',w.plant,name='addPlant'),
    path('shop/',w.shop,name='shop'),
    path('<int:shop_id>',w.shopdetails,name='shopdetails'),
    path('sellerdashboard/',w.sellerdashboard,name='sellerdashboard'),
    path('cart/',b.cart,name='cart'),
    path('add/<int:product_id>',b.add_to_cart,name='addtocart'),
    path('checkout/',b.checkout,name='checkout'),
    path('thankyou/',b.thankyou,name='thankyou'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
