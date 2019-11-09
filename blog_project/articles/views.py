from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'articles/post_list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'articles/post_detail.html'
    #context_object_name =  'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'articles/post_new.html'
    fields = ('title', 'body')

    def form_valid(self,form):
        form.inctance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model =Post
    template_name =  'articles/post_edit.html'
    fields =  ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'articles/post_delete.html'
    success_url = reverse_lazy('home')