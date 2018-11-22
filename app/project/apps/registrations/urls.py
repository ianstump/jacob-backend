from django.urls import path

from .views import RegistrationView, ValidationView

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('validation/', ValidationView.as_view(), name='registration_validation'),
]
