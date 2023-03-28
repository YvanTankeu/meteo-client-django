
from django.contrib import admin
from django.urls import path
from station import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donnees/', views.donnees, name='donnees'),
]
