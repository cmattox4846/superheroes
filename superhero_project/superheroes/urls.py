from django.urls.resolvers import URLPattern
from . import views
from django.urls import path


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/',views.detail, name ='detail' ),
    path('new/', views.create, name='create')
]