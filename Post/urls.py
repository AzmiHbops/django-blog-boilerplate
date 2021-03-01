from django.urls import path
from Post import views
import random
randnum1, randnum2 = random.randint(1, 12), random.randint(5, 15)

app_name = "post"
urlpatterns = [
    path('', views.home, name="home"),
    path(f'<int:pk>/{randnum1}/<slug:slug>/detail/', views.detail, name="detail"),
    path('new/', views.create, name="create"),
    path(f'<int:pk>/{randnum2}/<slug:slug>/edit/', views.edit, name="edit"),
    path(f'<int:pk>/{randnum2}/<slug:slug>/delete/', views.delete, name="delete")
]
