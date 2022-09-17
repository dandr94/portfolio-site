from django.urls import path

from portfolio.src.views import Home, Contacts

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('contacts/', Contacts.as_view(), name='contacts')
]
