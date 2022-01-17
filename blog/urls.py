from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]