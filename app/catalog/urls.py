from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wordstructures/', views.WordStructureView.as_view(), name='wordstructures'),
    path('wordstructure/<int:pk>', views.WordStructureDetailView.as_view(), name='wordstructure-detail'),
]