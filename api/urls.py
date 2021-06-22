from django.urls import path

from api import views

urlpatterns = [
    path('', views.post),
    path('file/<str:path>', views.get_file)
]
