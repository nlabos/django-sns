from django.views import generic
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def index(request):
    data = Post.objects.all()
    params = {
        'object_list': data
    }
    return render(request, 'post/home.html',params)