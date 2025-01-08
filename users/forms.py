from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    usable_password = None