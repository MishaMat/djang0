from django.urls import path
from . import views

urlpatterns = [
    path('forms/register/', views.Start.as_view()),
    path('forms/', views.NewsList.as_view()),
    path('forms/detail/<int:pk>/', views.NewsDetail.as_view()),
    path('forms/create/', views.Create.as_view()),
    path('forms/detail/<int:news_id>/edit/', views.Edit.as_view()),


]
