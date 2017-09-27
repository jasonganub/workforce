from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Job
from .serializers import JobSerializer


def job_detail(request, job_id):
    """
    View or update a job.
    """
    if request.method == 'GET':
        try:
            job = Job.objects.get(pk=job_id)
            serializer = JobSerializer(job)
            return JsonResponse(serializer.data)
        except Job.DoesNotExist:
            return HttpResponse(status=404)

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass


def create_job(request):
    """
    Create a job.
    """
    data = JSONParser().parse(request)
    serializer = JobSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
