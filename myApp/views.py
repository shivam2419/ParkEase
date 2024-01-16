from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,('index.html'))

def home(request):
    if request.method == "POST":
        uname = request.POST.get('owner_name')
        pnum = request.POST.get('Phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        parking_id = request.POST.get('parking_slot_id')

        submit = Register(owner_name = uname, vehicle_number = vehicle_number, 
        pnum = pnum, 
        parking_id = parking_id)
        submit.save()
    contexts = Register.objects.all()
    data={'data':contexts}
    return render(request,('home.html'), data)

def record(request):
    contexts = Register.objects.all()
    data={'data':contexts}
    return render(request,('record.html'), data)

def admin_page(request):
    return render(request,('admin.html'))

def search(request):
    if request.method == "POST":
        uname = request.POST.get('owner_name')
        pnum = request.POST.get('Phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        parking_id = request.POST.get('parking_slot_id')

        print(uname, pnum, vehicle_number, parking_id)
        submit = Register(owner_name = uname, vehicle_number = vehicle_number, 
        pnum = pnum, 
        parking_id = parking_id)
        submit.save()
        return redirect('home')
    return render(request,('search.html'))

def login(request):
    if request.method == "POST":
        uname = request.POST.get('userName')
        password = request.POST.get('password')
        id = request.POST.get('id')
        user = authenticate(request, user_name = uname, pswrd = password)
        if(user is not None):
            login(request, user)
            return redirect('home')
        else:
            # return HttpResponse("Username or password is incorrect!!")
            return redirect('home') #just for rough, for professional use, make it correct
        

        # check_data = signUp.objects.filter(id)
        #    value = check_data.pswrd
        # print(check_data)
        return redirect('index')
        
    
    return render(request,('login.html'))

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('userName')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('emailid')
        pnum = request.POST.get('phone_number')
        adhaar = request.POST.get('entry_date')

        if(password != confirm_password):
            return HttpResponse('Wrong password constraints')
        else:
            submit = signUp(user_name = uname, 
            pswrd = password,
            user_email = email,
            phone_num = pnum, 
            adhaar_image = adhaar
            )
            submit.save()
            return redirect('login')
        
    return render(request,('signup.html'))