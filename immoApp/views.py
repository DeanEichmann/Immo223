from django.shortcuts import render
from django.http import HttpResponse
from .models import estate
from django.template import loader
# Create your views here.
def index(request):
    estate_list = estate.objects.all()

    template = loader.get_template('immoApp/index.html')

    context = {
        'estate_list': estate_list,
    }
    return render(request, 'immoApp/index.html', context)

def details(request, estate_id):
    estateObj = estate.objects.get(pk=estate_id)

    context = {
        'estate':estateObj,
    }

    return render(request, 'estate/detail.html', context)