from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # name referenced in template logic statements
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]