from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from live.models import Profile,Hotel,Booking,Profile,Room, ROOM_TYPES


# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    
    if request.method == "POST":
        username= request.POST['username']
        email= request.POST['email']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['pnumber']
        user_type=request.POST['usertype']
        address=request.POST['address']

        exists= User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
            profile=Profile.objects.create(phone=phoneno,user_type=user_type,address=address,user=user)
            return redirect("/dashboard/")

    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "signin.html", {"message":"User account does not exists"})

        profile=user.profile
        print(profile.user_type)
        
        if profile.user_type == 1:
            return render(request,"hotel.html")
        
        if profile.user_type == 2:
            return render(request,"booking.html")


        if user is not None:
            login(request,user)
            return redirect("/")
            # Redirect to a success page.
        
        else:
            # Return an 'invalid login' error message.
            return render(request, "signin.html",{"message":"Enter the valid credentials"})

    return render(request,"signin.html")

def hotel(request):

    if request.method == "POST":
        hotelname= request.POST['hotelname']
        hotellocation= request.POST['hotellocation']
        hoteladdress= request.POST['hoteladdress']
        hotelstars= request.POST['stars']
        hotelimage= request.FILES['hotelimage']

        hotelexists= Hotel.objects.filter(hotel_name=hotelname).exists()

        if not hotelexists:
            hotel=Hotel.objects.create(hotel_name=hotelname,hotel_location=hotellocation,hotel_address=hoteladdress,hotel_stars=hotelstars,hotel_image=hotelimage)
            return redirect("/hoteldisplay/")
       
        if hotelexists:
           return redirect("/hoteldisplay/")

def hoteldisplay(request):
    hotel=Hotel.objects.all()
    return render(request,"display.html",{"hotels":hotel})

    # return render(request,"dashboard.html")

def dashboard(request):

    hotel = Hotel.objects.all()
    return render(request,"dashboard.html",{"hotels":hotel})

def booking(request, hotel_id):

    if request.method == "POST":
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        guests=request.POST['guests']
        room_type=request.POST['roomtype']
        print(room_type)
        user = request.user

        hotel = Hotel.objects.get(pk=hotel_id)
        room = Room.objects.get(hotel=hotel, room_type=room_type)


        booking=Booking.objects.create(checkin=checkin,checkout=checkout,num_guests=guests,room=room, user=request.user)
        return redirect("/booked/")

    hotel = Hotel.objects.get(pk=hotel_id)

    return render(request,"booking.html", {"hotel_rooms":ROOM_TYPES, "hotel_id":hotel_id})

def booked(request):

    user= request.user
    booking=Booking.objects.filter(user=user)
    print(booking)
    print(request.user)


    return render(request,"booked.html",{"Bookings":booking,"message":"Confirmed"})
    
def logout_view(request):
    logout(request)