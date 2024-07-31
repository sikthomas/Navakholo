from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', views.index, name='index'), 
    path('signup', views.signup, name='signup'),
    path('', views.login_view, name='login_view'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('personalInformation', views.personalInformation, name='personalInformation'), 
]