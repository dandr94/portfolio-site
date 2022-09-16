from django.urls import path

from portfolio.src.views import Home

urlpatterns = [
    path('', Home.as_view(), name='index'),
]
