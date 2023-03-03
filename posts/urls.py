
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', PostAPIList.as_view()),
    path('create/<int:pk>/', PostAPIUpdate.as_view()),
    path('delete/<int:pk>/', PostAPIDestroy.as_view()),

]