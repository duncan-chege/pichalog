from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

#import a package that looks for a variable called urlpatterns (a list). The package checks if the clients side url matches what's inside the list. If it matches, then it follows that path, then goes to the views py file
from . import views     #access our views

urlpatterns=[
    url('^$', views.base, name='base'),        #use of carets. $- anything before the url s considered
    url(r'^search/', views.search_results, name='search_results') 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)