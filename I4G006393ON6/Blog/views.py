from dataclasses import fields
from xml.parsers.expat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


class PostListView(generic.ListView):
    model = 'Post'


class PostCreateView(generic.CreateView):
    model = 'Post'
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")


class PostDetailView(model.Model):
    model = 'Post'


class PostUpdateView(generic.UpdateView):
    model = 'Post'
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")


class PostDeleteView(generic.DeleteView):
    model = 'Post'
    fields = "__all__"
    success_url = reverse_lazy("Blog:all")


# class AuthorCreateView(CreateView):
#     form_class = AuthorForm
#     template_name = 'author_new.html'
#     success_url = 'success'
