"""mario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
from django.conf.urls import url
# /from django.template.context_processors import static
from django.urls import path, include
from django.contrib import admin

# from django.contrib import admin
# from mario.accounts import views
# from mario.trueColleges import views
# from mario.trueColleges import views
# from mario.trueColleges.views import *
# /from mario.mario import settings

urlpatterns = [

    path('', include('trueColleges.urls')),
    # path(r'^search/$', search),
    # path('search', views.search, name='search'),
    url('admin/', admin.site.urls),
    # path('', views.ind, name='ind'),
    # path('signup', views.signup, name='signup'),
    # path('', views.search, name='search'),
    # path('login', views.login, name='login'),

    # url(r'^$', views.HomePage.as_view(), name='home'),
    # (r'^signin/$', views.SignIn.as_view(), name='signup'),
    # url(r'^login/$', views.LogIn.as_view(), name='login'),

]
# \\+static(settings.Colleges_URL, document_root=settings.Colleges_Root)
