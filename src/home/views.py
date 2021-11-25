from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

# Create your views here.

config={
  "apiKey": "AIzaSyCAKDrvyFr7Uzi87EiZ6XtH_IzrXNaxIkc",
  "authDomain": "betterbasket-64cdd.firebaseapp.com",
  "databaseURL": "https://betterbasket-64cdd-default-rtdb.firebaseio.com",
  "projectId": "betterbasket-64cdd",
  "storageBucket": "betterbasket-64cdd.appspot.com",
  "messagingSenderId": "1070615752292",
  "appId": "1:1070615752292:web:b53e0b06c317d8ccb8b971"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request) :
    item = database.child('better_basket').child('items').get().val()
    return render(request, 'home.html', {
        "item":item
    })

def login(request):
	return render(request, 'login.html')

def create(request):
    return render(request,'add.html')

def added(request):
    product = request.POST.get('product')

    quantity =request.POST.get('quantity')
    data = {
        "product":product,
        'quantity':quantity
    }
    database.child('shops').child('shp1').push(data)
    name = database.child('shops').child('shp1').get().val()
    return render(request,'added.html', {'e':name})

def login(request):
  return render(request, 'login.html')

def postlogin(request):
  email=request.POST.get('email')
  passw = request.POST.get('password')
  try:
    user = authe.sign_in_with_email_and_password(email,passw)
  except:
    message = "invalid cerediantials"
    return render(request,"login.html",{"msg":message})
  session_id=user['idToken']
  request.session['uid']=str(session_id)
  return render(request, "shops.html",{"e":email})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"login.html")

def signup(request):
 return render(request,"signup.html")

def postsignup(request):
  fname=request.POST.get("first_name")
  lname=request.POST.get("last_name")
  mail=request.POST.get('email')
  password = request.POST.get('birthday')
  country =request.POST.get('countrt')
  try:
    user=authe.create_user_with_email_and_password(mail,password)
    uid = user['localId']
    data={
      "first_name":fname,
      "last_name":lname,
      "country": country,

    }
    database.child("users").child(uid).child("details").set(data)
  except:
    message="Unable to create account try again"
    return render(request,"signup.html",{"messg":message})
  return render(request,"login.html")