from django.conf.urls import url        
#import a package that looks for a variable called urlpatterns (a list). The package checks if the clients side url matches what's inside the list. If it matches, then it follows that path, then goes to the views py file
from . import views     #access our views

urlpatterns=[
    url('^$', views.home_page, name='home_page')        #use of carets. $- anything before the url s considered
]