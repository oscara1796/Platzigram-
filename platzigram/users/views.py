"""Users Views """


from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#Exceptions

from django.db.utils import IntegrityError

#Models

from django.contrib.auth.models import User
from users.models import Profile


#Froms
from users.forms import ProfileForm

# Create your views here.

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
            profile.phone_number = data["phone_number"]
            profile.picture = data["picture"]
            profile.save()
            return redirect('update_profile')

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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, "users/login.html")

def signup_view(request):
    """Sign up view"""


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password does not match with password confirmation'})

        try:
            user = User.objects.create_user(username = username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already exists'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """logout view"""

    logout(request)

    return redirect('login')
