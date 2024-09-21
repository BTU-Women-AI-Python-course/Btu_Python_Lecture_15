# differences between **Session Authentication** and **Token Authentication**:

### **Session Authentication**:
- **Stateful**: The server maintains the user’s authentication state in a session. It stores the session information on the server-side and gives the client a session ID, usually stored in a browser cookie.
- **Web Application Centric**: Primarily used for traditional web applications where the client is a web browser.
- **Browser Cookie**: The session ID is stored in the user's browser and automatically sent with each request.
- **Server Load**: As the server stores session data for each user, it increases server load as the number of users grows.

### **Token Authentication**:
- **Stateless**: The server doesn’t store any session data. Instead, it issues a token to the client upon authentication, and the client sends this token with each request.
- **API and Mobile Friendly**: Token authentication is commonly used in mobile apps or when accessing APIs.
- **Flexibility**: The token can be stored on the client-side (local storage, session storage, etc.), and the client includes it in the request headers.
- **Scalable**: As the server does not need to maintain user sessions, it's more scalable in systems with many clients and APIs.

---

### **Example Code for Session Authentication (Django)**:
In a standard Django web application, you can authenticate using sessions like this:

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Creates a session for the user
            return redirect('home')  # Redirect after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
```

- After logging in, Django will create a session, and the browser will store the session ID in a cookie.
- On subsequent requests, the session ID will be sent to the server, and Django will identify the logged-in user.

---

### **Example Code for Token Authentication (Django REST Framework)**:
To use token authentication in Django REST Framework, you would implement something like this:

1. Install Django REST Framework and set up token authentication:
   ```bash
   pip install djangorestframework
   pip install djangorestframework-simplejwt
   ```

2. Configure Django settings:
   ```python
   # settings.py
   INSTALLED_APPS = [
       'rest_framework',
       'rest_framework.authtoken',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ],
   }
   ```

3. Generate tokens for users:
   ```python
   from rest_framework.authtoken.models import Token
   from django.contrib.auth.models import User

   # Create a token for a user
   user = User.objects.get(username='your_user')
   token = Token.objects.create(user=user)
   print(token.key)
   ```

4. API view that requires token authentication:
   ```python
   # views.py
   from rest_framework.decorators import api_view
   from rest_framework.response import Response
   from rest_framework.authentication import TokenAuthentication
   from rest_framework.permissions import IsAuthenticated

   @api_view(['GET'])
   @authentication_classes([TokenAuthentication])
   @permission_classes([IsAuthenticated])
   def my_api_view(request):
       return Response({"message": "Hello, you are authenticated!"})
   ```

- In this example, after a user logs in and gets a token, the token must be included in the **Authorization** header in each API request:

   ```bash
   curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/api/my_api_view/
   ```

With **Session Authentication**, the server stores session information.
With **Token Authentication**, the server validates a token sent with each request without maintaining server-side session data.

## Video explanation

[![YouTube Video](https://img.youtube.com/vi/UBUNrFtufWo/0.jpg)](https://www.youtube.com/watch?v=UBUNrFtufWo)
