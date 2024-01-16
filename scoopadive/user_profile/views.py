from django.contrib.auth.decorators import login_required
from django.db.models.functions import datetime

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from datetime import datetime

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

def view_modify_profile(request):
    current_user = request.user

    try:
        profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'user_profile/modify_profile.html', {"user": current_user, "profile": profile})


def calculate_age(birthdate):
    today = now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def modify_profile(request):
    profile = Profile.objects.get(user=request.user)

    # Get values from the form
    name = request.POST.get('name')
    student_id = request.POST.get('studentId')
    birthday = request.POST.get('birthday')
    name = request.POST.get('name')
    kisu = request.POST.get('kisu')
    dive_license = request.POST.get('diveLicense')
    introduction = request.POST.get('introduction')

    # Calculate age based on the provided birthdate
    age = calculate_age(birthday) if birthday else None

    major = request.POST.get('major')
    absence = request.POST.get('absence')
    image = request.POST.get('image')

    if name != '':
        profile.name = name
    if student_id != '':
        profile.studentID = student_id
    if birthday != '':
        profile.birthday = birthday
        profile.age = age
    if kisu != '':
        profile.kisu = kisu
    if dive_license != '':
        profile.diveLicense = dive_license
    if major != '':
        profile.major = major
    if introduction != '':
        profile.introduction = introduction
    if image != '':
        profile.image = image

    profile.is_absence = absence == 'on'

    profile.save()

    print("birthday: " + str(birthday) + "profile.birthday: " + str(profile.birthday))
    return render(request, 'main/home.html')
