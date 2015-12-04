from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    return render(request,'testbox/index.html')


def home(request):

    return render(request,'testbox/home.html')

def show_all_profiles(request,id):
    user = User.objects.get(pk=id)
    response = {
        'user' : user,
    }

    return render(request,'testbox/profile_page.html',response)