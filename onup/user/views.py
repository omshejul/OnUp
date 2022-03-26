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