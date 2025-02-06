
from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweetList, name='tweetList'),
    path('create/', views.TweetCreate, name='tweetCreate'),
    path('<int:tweet_id>/delete/', views.tweetDelete, name='tweetDelete'),
    path('<int:tweet_id>/update/', views.tweetUpdate, name='tweetUpdate'),
    path("register/",views.register, name="register")

    




]