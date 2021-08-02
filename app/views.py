from django.contrib import messages
from django.shortcuts import render
from .models import *


# Create your views here.
def cascade(request):
    disobj = DistrictModel.objects.all()
    pinobj = PincodeModel.objects.all()
    return render(request, 'index.html', {'District': disobj, 'Pincode': pinobj})

def person(request):
    if request.method == "POST":
        name = request.POST.get('name')
        district_id = request.POST.get('district')
        pincode_id = request.POST.get('pincode')
        district = DistrictModel.objects.get(pk=district_id)
        pincode = PincodeModel.objects.get(pk=pincode_id)

        Person(name=name, district = district.districtname, pincode=pincode.pincodeno).save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

