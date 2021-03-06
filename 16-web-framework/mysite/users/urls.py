from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('upload', views.upload_view, name='upload'),
    path('profile', views.profile_view, name='profile'),
    path('new_timesheet/', views.new_timesheet, name='start_pontaj'),
    path('stop_timesheet/', views.stop_timesheet, name='oprire_pontaj')
]
