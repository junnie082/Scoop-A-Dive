import re
from email import message

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

from user_profile.models import Profile
# View에 Model(Post 게시글) 가져오기
from .models import Log, Answer4Logs
from django.db.models import Q



def index(request):
    loglist = Log.objects.all()
    current_user = request.user

    if not isinstance(current_user, AnonymousUser):
        print("Is not AnonymousUser!")
        profile = Profile.objects.get(user=request.user)
        print("profile.is_ststMember: " + str(profile.is_ststMember))
        return render(request, 'main/index.html', {'loglist': loglist, 'profile': profile})
    else:
        return render(request, 'main/index.html', {'loglist': loglist})

def home(request):
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    loglist = Log.objects.all().order_by('-create_date')

    if kw:
        loglist = loglist.filter(
            Q(logName__icontains=kw)  | # 제목 검색
            Q(comments__icontains=kw) | # 내용 검색
            Q(location__icontains=kw) | # 위치 내용 검색
            Q(diver__icontains=kw)  # 질문 글쓴이 검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(loglist, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'main/home.html', {'loglist': page_obj, 'page': page, 'kw': kw})

def home_order_recommendation(request):
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    loglist = Log.objects.annotate(num_voters=Count('voter')).order_by('-num_voters', '-create_date')

    if kw:
        loglist = loglist.filter(
            Q(logName__icontains=kw)  | # 제목 검색
            Q(comments__icontains=kw) | # 내용 검색
            Q(location__icontains=kw) | # 위치 내용 검색
            Q(diver__icontains=kw)  # 질문 글쓴이 검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(loglist, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'main/home_order_recommendation.html', {'loglist': page_obj, 'kw': kw})


def posting(request, pk):
    page = request.GET.get('page', '1')  # Get the requested page number, default to 1 if not provided
    log = get_object_or_404(Log, pk=pk)  # Retrieve the specific log post using the provided primary key
    answer_list = Answer4Logs.objects.filter(log=log).order_by('-create_date')  # Retrieve the associated answers/comments for the log post
    paginator = Paginator(answer_list, 5)  # Set up pagination with 5 items per page
    page_obj = paginator.get_page(page)  # Get the requested page from the paginator

    return render(request, 'main/posting.html', {'user': request.user, 'log': log, 'answer_list': page_obj})


def new_log(request):
    if request.method == 'POST':
        if 'timeIn' in request.POST and 'timeOut' in request.POST:
            new_log = Log.objects.create(
                diver = request.user,
                logName = request.POST['logName'],
                diveNo = request.POST['diveNo'],
                date = request.POST['date'],
                location = request.POST['location'],
                timeIn = request.POST['timeIn'],
                timeOut = request.POST['timeOut'],
                weight = request.POST['weight'],
                barStart = request.POST['barStart'],
                barEnd = request.POST['barEnd'],
                maxDepth = request.POST['maxDepth'],
                minDepth = request.POST['minDepth'],
                temperature = request.POST['temperature'],
                comments = request.POST['comments'],
                images = request.FILES.get('images'),
                create_date = timezone.now()
            )

        return redirect('/home/')
    return render(request, 'main/new_log.html')


def remove_post(request, pk):
    log = Log.objects.get(pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('/home/')
    return render(request, 'main/remove_log.html', {'Log':  log})

def answer_create(request, logId):
    # 답글 추가
    log = get_object_or_404(Log, pk=logId)
    author = request.user
    content = request.POST.get('content')
    if content != '':
        log.answer4logs_set.create(content=content, author=author, create_date=timezone.now())
    return redirect('main:posting', logId)

def log_vote(request, log_id):
    log = get_object_or_404(Log, pk=log_id)
    if request.user in log.voter.all():
        log.voter.remove(request.user)
        log.save()
    else:
        if request.user == log.diver:
            message.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
        else:
            log.voter.add(request.user)
    return redirect('main:posting', log_id)

@login_required()
def view_modify_log(request, log_id):
    log = Log.objects.get(id=log_id)
    return render(request, 'main/modify_log.html', {'log_id': log_id, 'log': log})

@login_required
def modify_log(request, log_id):
    log = Log.objects.get(pk=log_id)
    logName = request.POST.get('logName')
    diver = request.POST.get('diver')
    diveNo = request.POST.get('diveNo')
    date = request.POST.get('date')
    location = request.POST.get('location')
    buddy = request.POST.get('buddy')
    timeIn = request.POST.get('timeIn')
    timeOut = request.POST.get('timeOut')
    weight = request.POST.get('weight')
    barStart = request.POST.get('barStart')
    barEnd = request.POST.get('barEnd')
    maxDepth = request.POST.get('maxDepth')
    minDepth = request.POST.get('minDepth')
    temperature = request.POST.get('temperature')
    comments = request.POST.get('comments')
    images = request.FILES.get('images')
    # try:
    #     images = request.FILES['images']
    # except MultiValueDictKeyError:
    #     images = None
    # print("logName: " + str(logName) + " diver: " + str(diver) + " diveNo: " + str(diveNo) + " date: " + str(date) + " location: " + str(location)
    #       + " buddy: " + str(buddy) + " timeIn: " + str(timeIn) + " timeOut: " + str(timeOut) + " weight: " + str(weight)
    #       + "barStart: " + str(barStart) + " barEnd: " + str(barEnd) + " maxDepth: " + str(maxDepth) + " minDepth: " + str(minDepth)
    #       + " temperature: " + str(temperature) + " comments: " + str(comments) + " images: " + str(images))

    if logName != '': log.logName = logName
    if diver != None: log.diver = diver
    if diveNo != '': log.diveNo = diveNo
    if date != '': log.date = date
    if location != '': log.location = location
    if buddy != '': log.buddy = buddy
    if timeIn != '': log.timeIn = timeIn
    if timeOut != '': log.timeOut = timeOut
    if weight != '': log.weight = weight
    if barStart != '': log.barStart = barStart
    if barEnd != '': log.barEnd = barEnd
    if maxDepth != '': log.maxDepth = maxDepth
    if minDepth != '':log.minDepth = minDepth
    if temperature != '':log.temperature = temperature
    if comments != '':log.comments = comments
    if images != '': log.images = images

    log.save()

    return redirect('main:posting', pk=log_id)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer4Logs, pk=answer_id)
    if request.method == "POST":
        content = request.POST.get('content')
        answer.content = content
        answer.save()

        return redirect('main:posting', pk=answer.log.id)
        # return render(request, 'main/posting.html', {'log': answer.log})
    return render(request, 'main/modify_answer.html')


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer4Logs, pk=answer_id)
    log_id = answer.log.id
    answer.delete()
    return redirect('main:posting', pk=log_id)

