from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import estate
from immoApp.forms import estateForm
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

def new_estate(request):
    form = estateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/estateForm.html', {'form':form})

def edit_estate(request, id):
    # fetch film
    estateObj = estate.objects.get(id=id)
    form = estateForm(request.POST or None, instance=estate)

    if form.is_valid():
        form.save()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/estateForm.html', {'form':form, 'estate':estateObj})

def delete_estate(request, id):
    estateObj = estate.objects.get(id=id)

    if request.method == 'POST':
        estateObj.delete()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/delete-estate.html', {'estate':estateObj})