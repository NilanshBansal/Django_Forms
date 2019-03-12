from django.shortcuts import render
from apptwo.models import AccessRecord,Topic,Webpage
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'apptwo/index.html',context=date_dict)

def help(request):
    return render(request, 'apptwo/help.html')
    