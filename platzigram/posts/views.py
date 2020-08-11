"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Forms
from posts.forms import PostForm

# Models
from posts.models import Post



class PostFeedView(LoginRequiredMixin, ListView):
    """Return all publisheed Posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    # paginate_by = 2
    context_object_name= 'posts'



# @login_required
# def list_posts(request):
#     """List existing posts."""
#     posts = Post.objects.all().order_by('-created')
#
#     return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print("Post is save")
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
