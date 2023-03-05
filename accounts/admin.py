from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PersonalUserChangeForm, PersonalUserCreationForm


PersonalUser = get_user_model()


class PersonalUserAdmin(UserAdmin):
    add_form = PersonalUserCreationForm
    form = PersonalUserChangeForm
    model = PersonalUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]


admin.site.register(PersonalUser, PersonalUserAdmin)
