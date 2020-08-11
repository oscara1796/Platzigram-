"""POSTS URLS"""

#Django
from django.urls import path



#views
from posts import views


urlpatterns =[
    path(
    route='',
    view= views.PostFeedView.as_view(),
    name="feed"
    ),

    path(
    route='posts/new/',
    view= views.create_post,
    name="create"
    ),

]
