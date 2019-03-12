from django.shortcuts import render,HttpResponse
from users.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    users_dict = {'users':users}
    return render(request,'users/index.html',context=users_dict)