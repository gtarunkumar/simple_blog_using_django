from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    # messages.success(request,'welcome')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        if(len(name)<2 or len(email)<6 or len(phone)<9 or len(content)<5):
            messages.error(request,"Please fill all the feilds correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your issue has been submitted succesfully! We will reach you soon!")
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>40 or len(query) < 1:
        allPosts=Post.objects.none()
    else:
        allPosts=Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts=allPosts.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request,"Please fill all the feilds correctly")
    params={'allPosts':allPosts,'query':query}
    return render(request,"home/search.html",params)
    # return HttpResponse("search")


def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['signupemail']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if(len(username) > 10):
            messages.error(request, "Your username must contain less than 10 characters!")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Your username must contain only charctaers and numbers!")
            return redirect('/')
        if(pass1 != pass2):
            messages.error(request, "password mismatch! ")
            return redirect('/')

        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "You are registered successfully!")
        return redirect('/')

    else:
        return HttpResponse("404 - page not found") 

def handleLogin(request):
    if request.method=='POST':
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']
        # print(loginemail,loginpassword)
        user = authenticate(username = loginemail,password = loginpassword)
        # print(user)

        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials! please check your email and password")
            return redirect('/')
    else:
        return HttpResponse("404 - page not found") 

def handleLogout(request):
    
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect("/")






