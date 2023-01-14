from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

# Create your views here.
class BlogListView(View):
   def get(self, request, *args, **kwargs):
      context = {

      }
      return render(request, 'blog_list.html',context)

class BlogCreateView(View):
   def get(self, request, *args, **kwargs):
      form = PostCreateForm()
      return render(request, 'blog_create.html',{'form':form})
   
   def post(self, request, *args, **kwargs):
      if request.method == 'POST':
          form = PostCreateForm(request.POST)
          if form.is_valid():
              title = form.cleaned_data.get('title')
              content = form.cleaned_data.get('content')

             # p, created = 
              
      return render(request, 'blog_create.html',{})