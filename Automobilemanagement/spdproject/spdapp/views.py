from  django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from math import ceil

from .forms import RegistrationForm, ProductForm, FeedbackForm
from .models import Registration, Admin, Product


def indexfunction(request):
    return render(request,"index.html")
def sparepart(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,'Spateparts.html',params)




def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/login')
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        Order = Orders(items_json=items_json, name=name, amount=amount, email=email, address1=address1,
                       address2=address2, city=city, state=state, zip_code=zip_code, phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id, update_desc="placed")
        update.save()
        thank = True
        id = Order.order_id
        oid = str(id)
        oid = str(id)
        param_dict = {

            'MID': 'PVzgWn17633192659045',
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


def registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registration Failed")

    return render(request,"registration.html",{"form":form})
def userlogin(request):
    return render(request,"userlogin.html")
def viewprodectsinad(request):
    return render(request,"viewprodectsinad.html")

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter( Q(email=emailid) & Q(password=pwd) )

    if flag:
        return render(request,"userhome.html")
    else:
        msg="Login Failed"
        return render(request, "userlogin.html",{"msg":msg})

def userhome(request):
    return render(request,"userhome.html")

def userlogout(request):
    return render(request,"userlogin.html")
def newproject(request):
    return render(request,"newproducts.html")
def addproduct(request):
    auname = request.session["auname"]
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addproduct.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"auname":auname,"productform":form})
def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html")

def viewaproducts(request):
    auname=request.session["auname"]
    productlist = Product.objects.all()
    count = Product.objects.count()
    return render(request,"viewaproducts.html",{"auname":auname,"productlist":productlist,"count":count})

def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})

def adminlogout(request):
    return render(request,"adminlogin.html")

def displayeproducts(request):

    eid=request.session["eid"]
    ename=request.session["ename"]

    pname = request.POST["pname"]
    print(pname)

    productlist = Product.objects.filter(name__icontains=pname)

    return render(request,"displayeproducts.html",{"eid": eid, "ename": ename,"productlist":productlist})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback_thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})








