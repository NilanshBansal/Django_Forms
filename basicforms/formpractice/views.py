from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def index(request):
    return HttpResponse('WELCOME !')

def form_add(request):
    form = forms.TestForm()

    if request.method == 'POST':
        form = forms.TestForm(request.POST)

        if form.is_valid():
            print('Validation succeess !')
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('DESCRIPTION: ' + form.cleaned_data['description'])

    return render(request,'formpractice/form.html',{'form':form})