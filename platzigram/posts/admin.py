from django.contrib import admin

# Register your models here.

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""

    list_display= ('pk','user','profile', 'title', 'photo')
    list_display_links = ('pk','user',)
    search_fields = ('user__email','user__first_name', 'user__last_name','title','user__username')

    list_filter = ('created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )

    fieldsets = (
    #Primer categoria
        ("Post", {
            'fields': (
            ('title','photo'),
            ),
        }
        ),

    #Segunda  caegoria
    ("META-DATA",{
        'fields':(
            ('user'),
            ('created','modified'),
        ),
    }),
    )


    readonly_fields = ('created', 'modified','user')
