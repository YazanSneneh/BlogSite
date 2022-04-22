from django.contrib.auth.models import User
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.utils import timezone
from django.views.generic import UpdateView
from django.urls import reverse
from .forms import PostForm
from .models import Post


def articles(request):
    try:
        queryset = get_list_or_404(Post)
    except:
        queryset = []
    return render(request, "blog/posts.html", {"articles": queryset})

def article_details(request, pk):
    article = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post.html", {"article": article})

# the same url request accept GET and POST method
def post_new(request):
    if request.method =="POST":
        # when form is POST request i need to pass data
        form = PostForm(request.POST)
        # check if form contains not empy and correct values
        if form.is_valid():
            # commit false, don't commit yet because i need to add extra info,
            # was not submitted in form
            post = form.save(commit=False)
            post.author = get_object_or_404(User, pk=2)

            post.published_date = timezone.now()
            post.save()
            return redirect('article_details', post.pk)   # redirect user to details
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request, pk):
    obj = get_object_or_404(Post, id=pk).delete()
    return redirect('articles')

class UpdatePost(UpdateView):
    model=Post
    template_name='blog/update_post.html'
    fields=['title', 'description', 'text']

    def get_success_url(self):
        return reverse('articles')
