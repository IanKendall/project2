from django.urls import path
from catalog import views as catalog_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', catalog_views.index, name='index'),
    path('wordstructures/', catalog_views.WordStructureView.as_view(), name='wordstructures'),
    path('wordstructure/<int:pk>', catalog_views.WordStructureDetailView.as_view(), name='wordstructure-detail'),
    path('hello-view/', catalog_views.HelloApiView.as_view()),
    path('worddata/', catalog_views.worddata_list),
    path('worddata/<int:pk>', catalog_views.worddata_detail),
]
