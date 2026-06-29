from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError(
                'Заполните либо имя, либо фамилию'
            )

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']