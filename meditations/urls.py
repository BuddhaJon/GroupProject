from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('med_list/', views.MeditationListView.as_view(), name='med_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('forgot/', views.ForgotPasswordView.as_view(), name='forgot'),
    # path('med_home/', views.MeditationHomeView.as_view(), name='med_home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
