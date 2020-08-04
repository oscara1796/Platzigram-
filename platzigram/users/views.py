"""Users Views """


from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse

#Model
from django.contrib.auth.models import User
from posts.models import Post
#Froms
from users.forms import ProfileForm, SignupForm

# Create your views here.

class UserDetailView(LoginRequiredMixin,DetailView):
    """User Detail View"""
    template_name = 'users/detail.html'
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name ='user'

    def get_context_data(self, **kwargs):
        """Add user´s post to context """
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


@login_required
def update_profile(request):
    """update a user´s profile"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            profile.website = data["website"]
            profile.biography = data["biography"]
            profile.phone_number = data["phone_number"];
            profile.picture = data["picture"];
            profile.save()
            url = reverse('users:detail', kwargs= {'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
    request = request,
    template_name= 'users/update_profile.html',
    context={
        'profile':profile,
        'user': request.user,
        'form':form
    })

def login_view(request):
    """login View"""
    if request.method == 'POST':
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(request, username=username, password=password);
        if user:
            login(request, user);
            return redirect('posts:feed');
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, "users/login.html")

def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name= 'users/signup.html',
        context={'form':form}
    )


@login_required
def logout_view(request):
    """logout view"""

    logout(request);

    return redirect('users:login');
