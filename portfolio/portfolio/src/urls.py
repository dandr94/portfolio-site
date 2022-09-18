from django.urls import path

from portfolio.src.views import Home, ShowContacts

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('contacts/', ShowContacts.as_view(), name='contacts')
]
