from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('signout/',views.logout,name='logout'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('get_question',views.get_question,name='get_question'),
    path('end_page',views.end_page,name='end_page'),
    ]
if settings.DEBUG is True:

	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
