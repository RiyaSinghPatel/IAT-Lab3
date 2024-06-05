from django.urls import path
from myapp import views1  

app_name = 'myapp'

urlpatterns = [
    path(r'', views1.index, name='index'),
    path('about/', views1.about, name='about'),
    path('<int:book_id>/', views1.detail, name='detail')
    ]

