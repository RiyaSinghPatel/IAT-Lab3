from django.urls import include, path
from django.shortcuts import render
from django.conf.urls import handler404
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('about/', views.about, name='about'),  # URL pattern for the about page
    path('admin/', admin.site.urls),
    path(r'myapp/', include('myapp.urls1')),
]
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404