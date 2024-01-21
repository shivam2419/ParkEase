from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from twilio.rest import Client
import myApp.keys_twilio as keys_twilio
import random
# Create your views here.
# getting the last id
queryset = signUp.objects.values_list('id')
last_id = 0
tup = ()
for i in queryset:
    tup = i
last_id = tup[0]
print(last_id)
def index(request):
    return render(request,('index.html'))

def home(request):
    check_data = signUp.objects.get(id=last_id)
    Username = check_data.user_name
    Phone_number = check_data.phone_num
    
    if request.method == "POST":
        uname = request.POST.get('owner_name')
        pnum = request.POST.get('Phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        parking_id = request.POST.get('parking_slot_id')

        submit = carRegister(owner_name = uname, vehicle_number = vehicle_number, 
        pnum = pnum, 
        parking_id = parking_id)
        submit.save()
    contexts = carRegister.objects.all()
    data={'data':contexts,
          'username':Username,
          'pnum':Phone_number}
    return render(request,('home.html'), data)

def record(request):
    contexts = carRegister.objects.all()
    data={'data':contexts}
    return render(request,('record.html'), data)

def admin_page(request):
    return render(request,('admin.html'))

def search(request):
    check_data = signUp.objects.get(id=last_id)
    Username = check_data.user_name
    Phone_number = check_data.phone_num
    if request.method == "POST":
        uname = request.POST.get('owner_name')
        pnum = request.POST.get('Phone_number')
        vehicle_number = request.POST.get('vehicle_number')
        parking_id = request.POST.get('parking_slot_id')

        print(uname, pnum, vehicle_number, parking_id)
        submit = carRegister(owner_name = uname, vehicle_number = vehicle_number, 
        pnum = pnum, 
        parking_id = parking_id)
        submit.save()
        return redirect('home')
    context = {'username':Username,
               'pnum':Phone_number}
    return render(request,('search.html'), context)

def login(request):
    if request.method == "POST":
        uname = request.POST.get('userName')
        password = request.POST.get('password')
        id = request.POST.get('id')
        user = authenticate(request, user_name = uname, pswrd = password)
        if(user is not None):
            login(request, user)
            return render(request,'home.html')
        else:
            data={'username':uname,
                  'pnum':password}
            # return HttpResponse("Username or password is incorrect!!")
            
            return render(request,'home.html', data) #just for rough, for professional use, make it correct
        

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
        if(password != confirm_password):
            return HttpResponse('Wrong password constraints')
        else:
            submit = signUp(user_name = uname, 
            pswrd = password,
            user_email = email,
            phone_num = pnum, 
            )
            submit.save()
            return redirect('home')
    str_len = len(user_number)
    context = {'number':user_number[3:str_len]}
    return render(request,('signup.html'),context)

def signedup(request):
    if request.method == "POST":
        user_otp = request.POST.get('otp')
        if(user_otp != otp):
            return HttpResponse('Wrong OTP entered')
        else:
            return redirect('Signup')

# User info section int 
user_number = keys_twilio.my_phone_number
otp = random.randint(1001, 9999)
otp = str(otp)
def send_msg(request):
    if(request.method == "POST"):
        client = Client(keys_twilio.account_sid, keys_twilio.auth_token)
        message = client.messages.create(
            body = "\nOne time password for ParkEase : " + otp,
            from_=  keys_twilio.twilio_number,
            to = keys_twilio.my_phone_number,
        )
        print("OTP : ", message.body)
    #change returning page when using official
    return render(request,('get_otp.html'))


def get_otp(request):
    print("Otp : ",otp)
    context = {'number' : user_number,
               'otp':otp}
    return render(request,('otp_page.html'), context)