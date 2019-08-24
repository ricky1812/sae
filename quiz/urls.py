from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('signout/',views.logout,name='logout'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('get_question',views.get_question,name='get_question'),
    ]
