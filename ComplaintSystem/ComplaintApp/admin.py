from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Building, Flat


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'age', 'salary', 'designation', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'salary', 'designation')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'age', 'salary', 'designation', 'groups', 'is_staff', 'is_active', 'password1', 'password2'),
        }),
    )
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Building)
admin.site.register(Flat)