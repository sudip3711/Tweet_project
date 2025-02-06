from django.shortcuts import render
from .models import Tweet
from .forms import TwwetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(req):
    return render(req,'index.html')

def tweetList(req):
    Tweets = Tweet.objects.all().order_by('-created_at')
    return render(req,'tweets_list.html',{'tweets': Tweets})

@login_required
def TweetCreate(req):
    if req.method == "POST":
        forms =TwwetForm(req.POST, req.FILES)
        if forms.is_valid():
           tweet= forms.save(commit=False)
           tweet.user = req.user
           tweet.save()
           return redirect('tweetList')
    else:
        form =TwwetForm()
    return render(req,'tweet_create.html',{'form':form})

@login_required
def tweetUpdate(req, tweet_id):
    tweet= get_object_or_404(Tweet,pk=tweet_id,user =req.user)
    if req.method == "POST":
        forms =TwwetForm(req.POST, req.FILES,instance=tweet)
        if forms.is_valid():
           tweet= forms.save(commit=False)
           tweet.user = req.user
           tweet.save()
           return redirect('tweetList')
    else:
        form =TwwetForm(instance=tweet)
    return render(req,'tweet_create.html',{'form':form})


@login_required
def tweetDelete(req ,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user =req.user)
    if req.method == "POST":
        tweet.delete()
        return redirect('tweetList')
    return render(req,'tweet_delete.html',{'tweet':tweet})


def register(req):
    if req.method == "POST":
       form = UserRegistrationForm(req.POST)
       if form.is_valid():
           user= form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(req,user)
           return redirect('tweetList')
    else:
        form =UserRegistrationForm()
    return render(req,'registration/register.html',{'form':form})
