from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

def Home(request):
    posts = Post.objects.all().order_by('-date_created')
    context = {
        'posts':posts
    }
    return render(request, 'post/listing.html', context)

def Post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request, 'post/post_detail.html', context)

def PostComment(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.post = post
            comments.user = request.user
            comments.save()
            return redirect('details', pk=post.pk) 
    else:
        form = CommentForm()
        context = {'form': form, 'post': post}
    return render(request, 'post/post_comment.html',context)
