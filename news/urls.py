from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.news_today,name = 'newsToday'),
    path('archives/<past_date>/',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:id>/' ,views.article,name='article'),
    path('new/article$', views.new_article, name='new-article'),
 
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)