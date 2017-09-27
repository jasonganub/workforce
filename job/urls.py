from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^$', views.create_job),
    url(r'^(?P<job_id>[0-9]+)/$', views.job_detail),
]
