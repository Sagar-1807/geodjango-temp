from django.shortcuts import render,get_object_or_404
from . models import Location
from . forms import LocationModelForm

# Create your views here.
def calculate_dist(request):

    obj=get_object_or_404(Location,id=1)
    form=LocationModelForm(request.POST or None)
    context={
        'distance':obj,
        'form':form,
    }
    return render(request,'locations/main.html',context)