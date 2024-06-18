from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from user_profile.models import Profile


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('main:index')

def signup(request):
    if request.method == 'POST':
        # Extract user registration data from the POST request
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        name = request.POST['name']
        is_ststMember = request.POST.get('is_ststMember', '') == 'on'

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'common/signup.html', {'error_message': 'Username already exists.'})

        # Check if the passwords match
        if password1 == password2:
            # Create a new user
            user = User.objects.create_user(username=username, password=password1, email=email)

            # Create a corresponding profile for the user
            profile = Profile.objects.create(
                user=user,
                name=name,
                is_ststMember=is_ststMember
            )

            # Redirect to the home page or another appropriate location after successful registration
            return redirect('/')
        else:
            # Render the signup page with an error message if passwords do not match
            return render(request, 'common/signup.html', {'error_message': 'Passwords do not match.'})
    else:
        # Render the signup page for GET requests
        return render(request, 'common/signup.html')


