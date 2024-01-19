from email import message

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone

from user_profile.models import Profile
# View에 Model(Post 게시글) 가져오기
from .models import Log

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
    loglist = Log.objects.all().order_by('-create_date')
    paginator = Paginator(loglist, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'main/home.html', {'loglist': page_obj})
    # postlist = Post.objects.all()
    # home.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    # return render(request, 'main/home.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    # # posthing.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    log = Log.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'user': request.user, 'log': log})

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
                images = request.POST['images'],
                create_date = timezone.now()
            )
            print("date: " + str(new_log.date))

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
    if request.user == log.diver:
        message.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        log.voter.add(request.user)
    return redirect('main:posting', log_id)

@login_required()
def view_modify_log(request, log_id):
    return render(request, 'main/modify_log.html', {'log_id': log_id})

@login_required
def modify_log(request, log_id):
    log = Log.objects.get(pk=log_id)
    print("log: " + str(log.diver))
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
    images = request.POST.get('images')
    print("logName: " + str(logName) + " diver: " + str(diver) + " diveNo: " + str(diveNo) + " date: " + str(date) + " location: " + str(location)
          + " buddy: " + str(buddy) + " timeIn: " + str(timeIn) + " timeOut: " + str(timeOut) + " weight: " + str(weight)
          + "barStart: " + str(barStart) + " barEnd: " + str(barEnd) + " maxDepth: " + str(maxDepth) + " minDepth: " + str(minDepth)
          + " temperature: " + str(temperature) + " comments: " + str(comments) + " images: " + str(images))

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

    return render(request, 'main/home.html')




