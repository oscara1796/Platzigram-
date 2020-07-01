"""User Admin Classes """

#Django
from  django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.

#Esta es una forma de registrar nuestro modelo profile la forma easy
# admin.site.register(Profile)

#Pero también podemos hacer una clase para customizar como se ve en el Admin

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""

    list_display= ('pk','user','phone_number', 'website', 'picture')
    list_display_links = ('pk','user',)
    list_editable = ('website', 'picture')
    search_fields = ('user__email','user__first_name', 'user__last_name','phone_number','user__username')

    list_filter = ('created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )


    fieldsets = (
    #Primer categoria
        ("Profile", {
            'fields': (
            ('user','picture'),
            ),
        }
        ),
    #Segunda categoria
    ("Extra info",{
        'fields':(
            ('website','phone_number'),
            ('biography'),
        ),
    }
    ),
    #Tercera caegoria
    ("META-DATA",{
        'fields':(
            ('created','modified'),
        ),
    }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""
    model= Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
    'username',
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
