from django.shortcuts import render

from user_profile.models import Profile


# Create your views here.
def index(request):
    members = Profile.objects.filter(is_ststMember=True)
    return render(request, 'happy_buddies/index.html', {'members': members})
