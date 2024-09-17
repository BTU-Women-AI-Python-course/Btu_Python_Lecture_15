# Override User Model

tutorial on how to override the Django user model by 
removing the `username` field and making the `email` field the username, along with configuring the custom user manager. 
We'll assume that all this will be done within a `user` app.

### Step 1: Create the `user` app
Start by creating a `user` app in your Django project if it doesn’t already exist.

```bash
python manage.py startapp user
```

### Step 2: Modify the `models.py` to create a custom user model
In the `user` app, you’ll create a custom user model that inherits from `AbstractBaseUser` and `PermissionsMixin`. The key differences from Django's default user model will be:
1. Remove the `username` field.
2. Use `email` as the unique identifier.
3. Create a custom user manager.

In `user/models.py`, add the following:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifiers for authentication
    instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where email is the unique identifier instead of username.
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
```

### Explanation:
- `CustomUser` inherits from `AbstractBaseUser` and `PermissionsMixin`.
- We replace the `username` field with `email`, making it the unique identifier.
- The `CustomUserManager` defines methods for creating regular and superusers. 
- We use `USERNAME_FIELD = 'email'` to specify that email should be used as the login field.
- `REQUIRED_FIELDS` contains fields that are required when creating a superuser (besides the password and the email, which is the username field).

### Step 3: Update `settings.py`
In your Django project’s `settings.py`, tell Django to use the custom user model by adding this line:

```python
AUTH_USER_MODEL = 'user.CustomUser'
```

This tells Django to use the `CustomUser` model in place of the default user model.

### Step 4: Create the User Model Migration
Now, run the migrations to create the database schema for your custom user model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Update the `admin.py`
If you want to manage the custom user model from the Django admin interface, update the `admin.py` file in the `user` app as follows:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances are defined by the UserAdmin class.
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
```

### Step 6: Creating Superuser
When creating a superuser, you will no longer be asked for a username but for an email:

```bash
python manage.py createsuperuser
```

### Step 7: Testing the User Model
To ensure everything works correctly:
- Try registering new users via the Django admin and through any registration forms you may have.
- Verify that the email is being used as the username for logging in.

### Step 8: Updating Views and Forms
If you're using Django's authentication views or custom forms, you'll need to update them 
to use the email field instead of the username. Here’s an example of how you might update the `AuthenticationForm`:

```python
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    class Meta:
        model = User
        fields = ['email', 'password']
```

### Final Notes:
- Ensure that any other views, forms, or serializers are updated to handle the new user model.
- Be sure to test the functionality throughout your application.

This tutorial gives a basic walkthrough of overriding the user model in Django by replacing the
`username` with `email`. Let me know if you need additional details or modifications!
