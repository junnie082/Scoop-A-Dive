from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Profile

@login_required
def view_profile(request):
    # Assuming the user is authenticated, request.user will be the current user instance
    current_user = request.user

    # Get the profile associated with the current user
    try:
        profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'user_profile/profile.html', {"user": current_user, "profile": profile})
