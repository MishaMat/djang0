from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdvListView.as_view()),
    path('advertisement/<int:pk>', views.AdvDetailView.as_view()),

]
