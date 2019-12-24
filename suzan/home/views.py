from django.shortcuts import render
from django.views.generic import    (ListView,
                                     DetailView,
                                     CreateView,
                                     UpdateView,
                                                 )
from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #dictionary ko keyword jastai bhayo aba
    ordering = ['-pub_date']


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title','pub_date','body','image'] #Creates form with these fields
    template_name = 'blog_form.html'

    def form_valid(self, form):
        #if any changes is to be made..its the place to write
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title','pub_date','body','image'] #Creates form with these fields
    template_name = 'blog_form.html'

    def form_valid(self, form):
        #if any changes is to be made..its the place to write
        return super().form_valid(form)