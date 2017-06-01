from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^train/', views.train, name='train'),
    url(r'^authenticate/', views.authenticate, name='authenticate'),
]