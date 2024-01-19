from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.models import Post


# Create your views here.

def index(request):
    page = request.GET.get('page', '1') # 페이지
    postList = Post.objects.order_by('date')
    paginator = Paginator(postList, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'board/board_home.html', {'postList': page_obj})

def detail(request, post_id):
    # 상세보기
    post = Post.objects.get(id=post_id)
    return render(request, 'board/detail.html', {'post': post})

def view_new_post(request):
    return render(request, 'board/new_post.html')

def new_post(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            postName = request.POST['postName'],
            writer=request.user,
            date=timezone.now(),
            content=request.POST['content'],
        )

    return redirect('board:index')

def remove_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/board/')
    return render(request, 'board/remove_post.html', {'Post': post})


def answer_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    writer = request.user
    content = request.POST.get('content')
    print("content: " + str(content))

    # Check if content is not None and not an empty string
    if content is not None and content.strip():
        post.answer4post_set.create(content=content, writer=writer, date=timezone.now())

    # Redirect to the detail view of the post (or any other desired URL)
    return redirect('board:detail', post_id=post_id)


def view_modify_post(request, post_id):
    return render(request, 'board/modify_post.html', {'post_id': post_id})


def modify_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    postName = request.POST.get('postName')
    date = timezone.now()
    content = request.POST.get('content')

    if postName != '': post.postName = postName
    if date != '': post.date = date
    if content != '': post.content = content

    post.save()

    return render(request, 'board/detail.html', {'post': post})
