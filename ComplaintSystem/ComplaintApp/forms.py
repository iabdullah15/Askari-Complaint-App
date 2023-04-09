from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm

from .models import CustomUser, Complaint
from django import forms
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'salary', 'designation', 'password1', 'password2', 'groups')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()
        return user

class CustomUserChangeForm(UserChangeForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'salary', 'designation', 'groups')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
            self.save_m2m()
        return user


class CustomUserAdminForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age', 'salary', 'designation', 'is_active', 'is_staff')


class CustomUserAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['email']


class RegisterComplaintForm(forms.ModelForm):

    class Meta:

        model = Complaint
        fields = ['ComplaintType', 'ComplaintDescription']