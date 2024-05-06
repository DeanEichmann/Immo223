from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Estate
from immoApp.forms import EstateForm
from django.template import loader
# Create your views here.
def index(request):
    estate_list = Estate.objects.all()

    template = loader.get_template('immoApp/index.html')

    context = {
        'estate_list': estate_list,
    }
    return render(request, 'immoApp/index.html', context)

def details(request, Estate_id):
    EstateObj = Estate.objects.get(pk=Estate_id)

    context = {
        'Estate':EstateObj,
    }

    return render(request, 'immoApp/detail.html', context)

def new_Estate(request):
    form = EstateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/EstateForm.html', {'form':form})

def edit_Estate(request, id):
    # fetch film
    EstateObj = Estate.objects.get(id=id)
    form = EstateForm(request.POST or None, instance=Estate)

    if form.is_valid():
        form.save()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/EstateForm.html', {'form':form, 'Estate':EstateObj})

def delete_Estate(request, id):
    EstateObj = Estate.objects.get(id=id)

    if request.method == 'POST':
        EstateObj.delete()
        return redirect('immoapp:index')
    
    return render(request, 'immoApp/delete-Estate.html', {'Estate':EstateObj})