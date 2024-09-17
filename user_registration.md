# User Registration

### 1. Set Up Your Django Project

First, create a new Django project and app if you haven’t already.

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp users
```

### 2. Configure Your Django Settings

In `myproject/settings.py`, make sure to add your new app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'users',
    ...
]
```

You should also configure the custom user model if you haven’t done so already. Assuming you’re using the default Django user model but with email as the username field:

```python
AUTH_USER_MODEL = 'users.CustomUser'
```

### 3. Define Your Custom User Model

In `users/models.py`, define a custom user model if needed. Here’s an example using `AbstractBaseUser` and `PermissionsMixin`:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
```

Run the following commands to create and apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create the User Form

Create a form to handle user registration in `users/forms.py`:

```python
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
```

### 5. Create the Registration View

In `users/views.py`, define the registration view:

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')  # redirect to login after registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
```

### 6. Create the Registration Template

Create `templates/register.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```

### 7. Configure URLs

Add the URL pattern for the registration view in `users/urls.py`:

```python
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

Include this URL configuration in the main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
```

### 8. Run the Development Server

Finally, run your Django development server:

```bash
python manage.py runserver
```

Now, you should be able to navigate to `http://127.0.0.1:8000/users/register/` to access your registration form.

### Summary

This tutorial walks you through setting up a Django project with a custom user model and registration form.
You define a custom user model, create a form with validation, implement a view to handle registration, and set up a template and URL routing.
