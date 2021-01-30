from django.views import generic
from django.shortcuts import redirect, render
from .models import Post,Favorite
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
        'object': data,
        'is_favorite': False
    }
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(owner = request.user).filter(content_id = data).count()
        if is_favorite > 0:
            params['is_favorite'] = True    
    return render(request, 'post/detail.html',params)

@login_required
def post_delete(request,pk):
    if request.method == 'POST':
        data = Post.objects.get(pk = pk,owner = request.user)
        data.delete()
        messages.success(request,'メッセージを削除しました')
    else:
        messages.error(request,'正しい方法で削除してください')
    return redirect(to='/')

@login_required
def post_favorite(request,pk):
    if request.method == 'POST':
        # favoriteする投稿を取得
        data = Post.objects.get(pk = pk)
        # 自分が既にfavoriteしているか確認
        is_favorite = Favorite.objects.filter(owner = request.user).filter(content_id = data).count()
        if is_favorite > 0:
            messages.error(request, '既にそのメッセージにはお気に入り登録をしています。')
            return redirect(to='/')
        
        data.favorite_count += 1
        data.save()
        favorite = Favorite()
        favorite.owner = request.user
        favorite.content_id = data
        favorite.save()
        messages.success(request,'メッセージをお気に入りに登録しました')
    else:
        messages.error(request,'正しい方法でお気に入りに登録してください')
    return redirect(to='/')

def index(request,num=1):
    data = Post.objects.all()
    page = Paginator(data, 5)
    params = {
        'object_list': page.get_page(num)
    }
    return render(request, 'post/home.html',params)
