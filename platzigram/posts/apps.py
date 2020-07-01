"""Posts Application Module """

from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    #Cambia el nombre para los usuarios !
    verbose_name = "Posts"
