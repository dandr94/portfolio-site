from django.urls import path

from portfolio.src.views import Home, ShowContacts, AboutDetails, CertificateDetails

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('contacts/', ShowContacts.as_view(), name='contacts'),
    path('about_me/', AboutDetails.as_view(), name='about'),
    path('certificates/', CertificateDetails.as_view(), name='certificates')
]
