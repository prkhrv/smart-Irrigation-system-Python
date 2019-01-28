from django.shortcuts import render
from irrigation_app.models import CropData
from .irrigation import smart_irrigation
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    values = ""
    if request.method == "POST":
        name = request.POST.get('crop')
        values = CropData.objects.filter(crop_name = name).values_list('moisture_value',flat=True).get()
        key = request.POST.get('toggle')
        if(key == "ON"):
            smart_irrigation(values,1)

    return render(request,'index.html',{'values':values,})
