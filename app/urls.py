"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from register import views as reg_views
from django.conf import settings #needs to change for deployment
from django.conf.urls.static import static #needs to change for deployment


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #pulling all urls "included" in main (site shell) app folder
    path('signup/', reg_views.register, name='register'), #here we create the path to our modified user signup form
    path('profile/', reg_views.profile, name="profile page"),
    path('', include('django.contrib.auth.urls')), #this allows us to use djangos pre built froms from the contrib auth app django has
    #password reset routes
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'), name="password_reset_complete"),
    #pwa urls
    path('', include('pwa.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #needs to change for deployment
