from django.views import generic
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required
def create_post(request):
    # 送信時実行
    if request.method == 'POST':
        content = request.POST['content']
        user = request.user
        # モデルに保存
        post = Post()
        post.content = content
        post.owner = user
        post.save()
        messages.success(request,'新しいメッセージを投稿しました。')
        return redirect(to='/')
    # それ以外
    else:
        form = PostForm()
    params = {
        'form': form 
    }
    return render(request, 'post/create.html',params)

def post_detail(request,pk):
    data = Post.objects.get(pk = pk)
    params = {
        'object': data 
    }
    return render(request, 'post/detail.html',params)

def post_delete(request,pk):
    if request.method == 'POST':
        data = Post.objects.get(pk = pk)
        data.delete()
        messages.success(request,'メッセージを削除しました')
    else:
        messages.error(request,'正しい方法で削除してください')
    return redirect(to='/')

def index(request,num=1):
    data = Post.objects.all()
    page = Paginator(data, 5)
    params = {
        'object_list': page.get_page(num)
    }
    return render(request, 'post/home.html',params)
