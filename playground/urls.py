from django.urls import path
from . import views

app_name = 'playground'

urlpatterns = [
    path('home/', views.welcome, name='home'), # {{url 'playground-urls:home'}}
    path('hello/<str:name>/', views.hello_user, name='hello_user'),
    path('<int:num>/', views.print_one, name='print_num')

]