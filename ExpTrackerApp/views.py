import datetime
from django.shortcuts import render, redirect
from .models import ExpTracker
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    expenses = ExpTracker.objects.all().values()
    template = loader.get_template('disp.html')
    context = {
        'expenses': expenses
    }
    return HttpResponse(template.render(context, request))



def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))



def addrecord(request):
    x = request.POST['description']
    y = request.POST['amount']
    exp = ExpTracker(description = x, amount = y)
    exp.save()
    return HttpResponseRedirect(reverse('index'))



def delete(request, id):
    expen = ExpTracker.objects.get(id = id)
    expen.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    expenses = ExpTracker.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'expenses': expenses
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    descrip = request.POST['description']
    amt = request.POST['amount']
    expen = ExpTracker.objects.get(id = id)
    expen.description = descrip
    expen.amount = amt
    expen.save()
    return HttpResponseRedirect(reverse('index'))