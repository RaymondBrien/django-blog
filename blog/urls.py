from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home') # name can be referenced in template logic statements
]