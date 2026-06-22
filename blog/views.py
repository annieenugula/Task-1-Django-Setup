from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category, Comment
from .forms import UserRegisterForm, PostForm, CommentForm


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='published')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')

    else:
        form = UserRegisterForm()

    return render(request, 'blog/register.html', {'form': form})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')


def add_comment(request, slug):
    return redirect('home')


class CategoryPostsView(ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        category = get_object_or_404(
            Category,
            slug=self.kwargs['slug']
        )

        return Post.objects.filter(
            category=category,
            status='published'
        )