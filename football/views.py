from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib import auth
# Create your views here.
def start(request):
    context = {'username': auth.get_user(request).username}
    return render_to_response('football/start.html', context)


def info(request):
    context = {'username': auth.get_user(request).username}
    return render_to_response('football/info.html', context)