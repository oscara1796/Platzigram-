"""USERS URLS"""

# django
from django.urls import path


from users import views


urlpatterns= [

    #Posts
    path(
        route='profile/<str:username>/',
        view= views.UserDetailView.as_view(),
        name='detail'
    ),

    #Management
    path(
    route='users/login/',
    view= views.login_view,
    name="login"
    ),

    path(
    route='users/logout/',
    view= views.logout_view,
    name="logout"
    ),

    path(
    route='users/signup/',
    view= views.signup_view,
    name="signup"
    ),

    path(
    route='users/me/profile/',
    view= views.update_profile,
    name="update_profile"
    ),

]
