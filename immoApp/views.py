from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Estate
from .forms import EstateForm
from django.template import loader

def index(request):
    estate_list = Estate.objects.all()
    context = {'estate_list': estate_list}
    return render(request, 'immoapp/index.html', context)

def details(request, Estate_id):
    estate = get_object_or_404(Estate, pk=Estate_id)
    context = {'estate': estate}
    return render(request, 'immoapp/detail.html', context)

@login_required
@transaction.atomic
def new_Estate(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.author = request.user
            estate.save()
            # Trigger the prediction process here if applicable
            return redirect('immoapp:index')
    else:
        form = EstateForm()
    return render(request, 'immoapp/estateForm.html', {'form': form})

@login_required
@transaction.atomic
def edit_Estate(request, id):
    estate = get_object_or_404(Estate, id=id)
    if request.method == 'POST':
        form = EstateForm(request.POST, instance=estate)
        if form.is_valid():
            form.save()
            # Trigger the prediction process here if applicable
            return redirect('immoapp:index')
    else:
        form = EstateForm(instance=estate)
    return render(request, 'immoapp/estateForm.html', {'form': form, 'estate': estate})

@login_required
def delete_Estate(request, id):
    estate = get_object_or_404(Estate, id=id)
    if request.user != estate.author:
        return HttpResponseForbidden("You are not allowed to delete this property")
    if request.method == 'POST':
        estate.delete()
        return redirect('immoapp:index')
    return render(request, 'immoapp/delete-estate.html', {'estate': estate})