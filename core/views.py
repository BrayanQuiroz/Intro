from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *args, **kwargs):
      return render(request,'index.html',{})