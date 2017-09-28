from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^$', views.create_applicant),
    url(r'^(?P<app_id>[0-9]+)/$', views.applicant_detail),
]
