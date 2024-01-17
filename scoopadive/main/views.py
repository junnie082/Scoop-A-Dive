from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, get_object_or_404
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
    loglist = Log.objects.all()
    return render(request, 'main/home.html', {'loglist': loglist})
    # postlist = Post.objects.all()
    # home.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    # return render(request, 'main/home.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    # # posthing.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    log = Log.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'user': request.user, 'log': log})

def new_post(request):
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
            )
        # if request.POST['mainphoto']:
        #     new_article = Post.objects.create(
        #         postname=request.POST['postname'],
        #         contents=request.POST['contents'],
        #         mainphoto=request.POST['mainphoto'],
        #     )
        # else:
        #     new_article = Post.objects.create(
        #         postname=request.POST['postname'],
        #         contents=request.POST['contents'],
        #         mainphoto=request.POST['mainphoto'],
        #     )
        return redirect('/home/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    log = Log.objects.get(pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('/home/')
    return render(request, 'main/remove_post.html', {'Log':  log})

def answer_create(request, logId):
    # 답글 추가
    log = get_object_or_404(Log, pk=logId)
    author = request.user
    log.answer_set.create(content=request.POST.get('content'), author=author)
    return redirect('main:posting', logId)