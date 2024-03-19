from django.shortcuts import render,redirect
from .forms import CustRegForm,staffRegForm,BookingForm,RoomForm
from .models import customer,staff,Room,Booking
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request,'Home.html')

def aboutus(request):
    return render(request,'Aboutus.html')

def contact(request):
    return render(request,'Contact.html')

def customerReg(request):
    form = CustRegForm()
    if request.method == "POST":
        form = CustRegForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customerlogin')
    return render(request,'CustomerRegistration.html',{'form':form})   

def login(request):
    return render(request,'login.html')

def customerlogin(request):
    form = CustRegForm()
    return render(request,'customerlogin.html',{'form':form})

  

def customerlog(request):
    if request.method=='POST':
        name= request.POST.get('name')
        password= request.POST.get('password')
        cr= customer.objects.filter(name=name,password=password)
        if cr:
            user_details=customer.objects.get(name=name,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
            email=user_details.email



            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            request.session['email']=email

            return redirect('customerprofile')
        else:
            form = CustRegForm()
            ce="Invalid Username or Password"
            return render(request,'customerlogin.html',{'ce':ce,'form':form})
    else:
        return render(request,'login.html')  
    

def customerprofile(request):
    name=request.session['name']
    cr=customer.objects.get(name=name)
    return render(request,'customerprofile.html',{'cr':cr})

def customerupdate(request,name):
    cr = customer.objects.get(name=name)
    form = CustRegForm(instance= cr)
    if request.method=="POST":
        form = CustRegForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('customerprofile')
    return render(request, "customerupdate.html",{'form':form})


def staffReg(request):
    form = staffRegForm()
    if request.method == "POST":
        form = staffRegForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stafflogin')
    return render(request,'staffregister.html',{'form':form}) 

def stafflogin(request):
    form = staffRegForm()
    return render(request,'stafflogin.html',{'form':form})

def stafflog(request):
    if request.method=='POST':
        name= request.POST.get('name')
        password= request.POST.get('password')
        cr= staff.objects.filter(name=name,password=password,loginapproval=True)
        cm= staff.objects.filter(name=name,password=password,loginapproval=False)
        if cr:
            user_details=staff.objects.get(name=name,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
            email=user_details.email



            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            request.session['email']=email

            return redirect('staffprofile')
        elif cm:
            form = staffRegForm()
            ce="Wait for Admin Approval"
            return render(request,'stafflogin.html',{'ce':ce,'form':form})
        else:
            form = staffRegForm()
            ce="Invalid Username or Password"
            return render(request,'stafflogin.html',{'ce':ce,'form':form})
    else:
        return render(request,'login.html')  
    

def staffprofile(request):
    name=request.session['name']
    cr=staff.objects.get(name=name)
    return render(request,'staffprofile.html',{'cr':cr})  

def staffupdate(request,name):
    cr = staff.objects.get(name=name)
    form = staffRegForm(instance= cr)
    if request.method=="POST":
        form = staffRegForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('staffprofile')
    return render(request, "staffupdate.html",{'form':form})


def viewroom(request):
    cr = Room.objects.all()
    return render(request,"viewrooms.html",{'cr':cr}) 

def bookroom(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customerprofile')
    return render(request,'booking.html',{'form':form}) 

def staffviewroom(request):
    cr = Room.objects.all()
    return render(request,"staffviewrooms.html",{'cr':cr}) 

def updateroom(request,pk):
    cr = Room.objects.get(id=pk)
    form = RoomForm(instance= cr)
    if request.method=="POST":
        form = RoomForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('staffviewroom') 
    return render(request, "updateroom.html",{'form':form}) 

def viewbookings(request):
    cr = Booking.objects.all()
    return render(request,"viewbookings.html",{'cr':cr}) 

def logoutuser(request):
    logout(request)
    return redirect("login") 
