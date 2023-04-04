from django.urls import path,include
from sculptorapp import views
urlpatterns = [
    path('',views.home,name='home')
]
