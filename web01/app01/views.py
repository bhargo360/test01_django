from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import App01

def app01(request):
    mymembers = App01.objects.all().values()
    template = loader.get_template('template02.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))