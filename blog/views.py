# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

# Create your views here.
class FirstView(generic.DetailView):
  template_name = ''
  def get(self,request):
    print "GET REQUEST CALLED"
    return 
  
  def post(self, request, *args, **kwargs):
		print (request.POST)
    return
