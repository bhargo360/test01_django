from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app01(request):
    template = loader.get_template('template01.html')
    return HttpResponse(template.render())