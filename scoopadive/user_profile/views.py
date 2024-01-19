from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import datetime

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from datetime import datetime

from main.models import Log
from .api import check_major
from .models import Profile

@login_required
def view_profile(request, user_id):
    user = get_object_or_404(User, username=user_id)
    profile = get_object_or_404(Profile, user=user)
    # Assuming the user is authenticated, request.user will be the current user instance
    # Filter Log objects for the current user
    loglist = Log.objects.filter(diver=user_id)

    return render(request, 'user_profile/profile.html', {"user_id": user_id, "profile": profile, "loglist" : loglist})

def view_modify_profile(request, user_id):
    current_user = request.user
    majors = check_major()
    try:
        profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'user_profile/modify_profile.html', {"user_id": user_id, "user": current_user, "profile": profile, "majors": majors})


def calculate_age(birthdate):
    today = now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def modify_profile(request, user_id):
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

    return redirect('main:home')

