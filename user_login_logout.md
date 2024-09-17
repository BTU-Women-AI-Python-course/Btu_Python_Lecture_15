# User Login and Logout

### 1. Create the Login Form

Django provides a built-in `AuthenticationForm` that you can use for login. You don't need to create a custom form for basic login functionality.

### 2. Create the Login View

Define the login view in `users/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')  # Redirect to a homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
```

### 3. Create the Logout View

Define the logout view in `users/views.py`:

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page or homepage
```

### 4. Create the Login Template

Create `templates/login.html` for the login form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
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

### 5. Configure URLs

Add the URL patterns for login and logout in `users/urls.py`:

```python
from django.urls import path
from .views import login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
```

### 6. Protect Views and Redirect After Login

To protect views that require authentication, use Django’s `login_required` decorator. For example, in `users/views.py`:

```python
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')
```

In `urls.py`, make sure to include this view:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('home/', home, name='home'),
]
```

Make sure you have a view and template for `home` (or whichever protected page you are using).

### Summary

1. **Login**: Create a view using `AuthenticationForm` and handle POST requests for user authentication.
2. **Logout**: Use `auth_logout` to log out users and redirect them appropriately.
3. **Templates**: Provide simple HTML forms for login and display messages.
4. **URLs**: Add URL patterns for login and logout, and protect views using `login_required`.

You can now manage user authentication in your Django project with these basic views and templates.
