from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.models import Post, Answer4Post


# Create your views here.

def index(request):
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    postlist = Post.objects.order_by('-date')

    if kw:
        postlist = postlist.filter(
            Q(postName__icontains=kw)  | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(writer__icontains=kw) # 글쓴이 검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(postlist, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'board/board_home.html', {'postlist': page_obj})

def index_order_recommendation(request):
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    postlist = Post.objects.annotate(num_voters=Count('voter')).order_by('-num_voters', '-date')

    if kw:
        postlist = postlist.filter(
            Q(postName__icontains=kw)  | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(writer__icontains=kw)  # 글쓴이 검색
            # Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(postlist, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'board/board_home_order_recommendation.html', {'postlist': page_obj})


def detail(request, post_id):
    # 상세보기
    page = request.GET.get('page', '1') # Get the requested page number, default to 1 if not provided
    post = Post.objects.get(id=post_id)
    answer_list = Answer4Post.objects.filter(post=post).order_by('-date')
    paginator = Paginator(answer_list, 5) # Set up pagination with 5 items per page
    page_obj = paginator.get_page(page) # Get the requested page from the paginator

    return render(request, 'board/detail.html', {'post': post, 'answer_list': page_obj})

def view_new_post(request):
    return render(request, 'board/new_post.html')

def new_post(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            postName = request.POST['postName'],
            writer=request.user,
            date=timezone.now(),
            content=request.POST['content'],
            images=request.FILES.get('images')
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

    # Check if content is not None and not an empty string
    if content is not None and content.strip():
        post.answer4post_set.create(content=content, writer=writer, date=timezone.now())

    # Redirect to the detail view of the post (or any other desired URL)
    return redirect('board:detail', post_id=post_id)


def view_modify_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'board/modify_post.html', {'post_id': post_id, 'post': post})


def modify_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    postName = request.POST.get('postName')
    date = timezone.now()
    content = request.POST.get('content')
    images = request.FILES.get('images')


    if postName != '': post.postName = postName
    if date != '': post.date = date
    if content != '': post.content = content
    if images != '': post.images = images

    post.save()

    return redirect('board:detail', post_id=post_id)

@login_required(login_url='common:login')
def post_vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    recommended = False
    if request.user in post.voter.all():
        post.voter.remove(request.user)
        post.save()
    else:
        post.voter.add(request.user)

    return redirect('board:detail', post_id=post.id)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer4Post, pk=answer_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        answer.content = content
        answer.save()

        return redirect('board:detail', post_id=answer.post.id)
    return render(request, 'board/modify_answer.html')

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer4Post, pk=answer_id)
    answer.delete()
    return redirect('board:detail', post_id=answer.post.id)
