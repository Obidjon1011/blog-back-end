from django.urls import path
from .views import *

urlpatterns = [
    path('<str:slug>/', ArticleDetail.as_view(), name='detail'),
    path('', ArticleList.as_view()),
    path('catagory/', TagList.as_view()),
]