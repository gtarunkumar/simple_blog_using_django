from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Post,BlogComment
from blog.templatestags import extras

# Create your views here.
# def home(request):
#     return HttpResponse("home")
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)


def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
        if(reply.parent.sno not in repDict.keys()):
            repDict[reply.parent.sno]=[reply]
        else:
            repDict[reply.parent.sno].append(reply)
    context = {'post':post,'comments':comments,'user':request.user,'replyDict':repDict}
    return render(request,'blog/blogPost.html',context)


def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            messages.success(request,"Comment posted successfully!")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Reply posted successfully!")
        comment.save()    
    return redirect(f'/blog/{post.slug}')