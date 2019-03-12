from django.shortcuts import render,HttpResponse
from users.models import User
from users.forms import NewUserForm
# Create your views here.

def index(request):
    users = User.objects.all()
    users_dict = {'users':users}
    return render(request,'users/index.html',context=users_dict)

def signup(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid !')

    return render(request,'users/sign_up.html',{'form':form})