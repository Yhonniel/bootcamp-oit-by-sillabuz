from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your Username'
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password'
            }
        )
    )
