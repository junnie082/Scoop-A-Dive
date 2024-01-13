from django.shortcuts import render, redirect
# View에 Model(Post 게시글) 가져오기
from .models import Post, Log

def index(request):
    loglist = Log.objects.all()
    return render(request, 'main/index.html', {'loglist': loglist})

def home(request):
    loglist = Log.objects.all()
    return render(request, 'main/home.html', {'loglist': loglist})
    # postlist = Post.objects.all()
    # home.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    # return render(request, 'main/home.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    # post = Post.objects.get(pk=pk)
    # # posthing.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    # return render(request, 'main/posting.html', {'post':post})
    log = Log.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'log': log})

def new_post(request):
    if request.method == 'POST':
        if 'timeIn' in request.POST and 'timeOut' in request.POST:
            new_log = Log.objects.create(
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