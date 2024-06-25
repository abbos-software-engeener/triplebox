from django.urls import path 
from .views import *

urlpatterns = [
    path('house/',HouseListView.as_view()),
    path('house/<int:pk>/',HouseDetailView.as_view()),
    path('client-create/',ClientCreateView.as_view()),

]