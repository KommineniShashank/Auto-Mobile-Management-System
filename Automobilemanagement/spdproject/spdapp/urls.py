from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("",views.indexfunction,name="index"),
    path("registration", views.registration, name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('checkadminlogin', views.checkadminlogin, name="checkadminlogin"),
    path('adminhome', views.adminhome, name="adminhome"),
    path("viewaproducts", views.viewaproducts, name="viewaproducts"),
    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("newproducts",views.newproject,name="newproducts"),
    path("spareparts",views.sparepart,name="spareparts"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("feedback",views.feedback_view,name="feedback"),
path('checkout',views.checkout,name="checkout"),
   ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
