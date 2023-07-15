#blog/views.py


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy, reverse # new
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Review



class BlogListView(ListView):
    model=Post
    template_name="post_list.html"

class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=['title', "body"]

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class ReviewCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk) :
        f = get_object_or_404(Post, id=pk)
        review = Review(review=request.POST['review'], author=request.user, post=f)
        review.save()
        return redirect(reverse('blog:post_detail', args=[pk]))

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "blog/post_review_delete.html"
   
    
    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        post = self.object.post
        return reverse(reverse('blog:post_detail', args=[pk]))
