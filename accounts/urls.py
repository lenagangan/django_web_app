from django.conf.urls import url
from django.urls import path
from .views import my_profile

app_name = 'accounts'

urlpatterns = [
	url(r'^', my_profile, name='my_profile')
]
