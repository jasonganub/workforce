from django.conf.urls import include, url
from django.contrib import admin
from job.models import Job
from job.serializers import JobViewSet, JobSerializer
from rest_framework import routers, serializers, viewsets



router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
