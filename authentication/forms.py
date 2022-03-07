from django import forms
from django.contrib.auth import get_user_model

from .models import User

User = get_user_model()

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password'] 

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError("email ja existe!")
        return email
    
    def save(self, commit: bool = True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
