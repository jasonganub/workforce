from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from job import urls
from job.serializers import JobViewSet, JobSerializer
from experience.serializers import ExperienceViewSet
from applicant.serializers import ApplicantViewSet


urlpatterns = [
    url(r'^jobs/', include('job.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
