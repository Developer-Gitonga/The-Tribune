from django.urls import path
from . import views

urlpatterns=[
    path('', views.welcome, name = 'welcome'),
    path('today/',views.news_of_day,name = 'newsToday'),
    path('archives/<past_date>',views.past_days_news,name = 'pastNews')
]