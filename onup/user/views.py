 from django.shortcuts import render
from django.http.response import HttpResponse

import pyrebase
 

config={
    "apiKey": "AIzaSyCXnY_yxEYdsde2V6-riUxYFTZVn8yKSkw",
    "authDomain": "onup-codebreak.firebaseapp.com",
    "databaseURL": "https://onup-codebreak-default-rtdb.firebaseio.com/",
    "projectId": "onup-codebreak",
    "storageBucket": "onup-codebreak.appspot.com",
    "messagingSenderId": "350537350064",
    "appId": "1:350537350064:web:4af427c4feda7df9bd34754",
    "measurementId": "G-E43K5HSY33"
}



firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        projectname = database.child('Projectname').get().val()
    
        context = {
            'projectname':projectname
        }
        return render(request, 'index.html', context)

def dashboard(request):
    return render(request,'dash/index.html')
def page404(request):
    return render(request,'dash/404.html')
def page500(request):
    return render(request,'dash/500.html')
def charts(request):
    return render(request,'dash/charts.html')
def tables(request):
    return render(request,'dash/tables.html')
def login(request):
    return render(request,'dash/login.html')
def password(request):
    return render(request,'dash/password.html')
def register(request):
    return render(request,'dash/register.html')
def poll(request):
    return render(request,'dash/poll.html')
def light(request):
    return render(request,'dash/layout-sidenav-light.html')