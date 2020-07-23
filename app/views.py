from django.shortcuts import render
from .models import Jobs
from .serializers import JobsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def list_jobs(request):
	all_jobs = Jobs.objects.all()
	return render(request, 'jobs.html', {'all_jobs': all_jobs})


@api_view(['GET'])
def get_jobs(request):
	location = request.query_params.get('location', None)
	job_type = request.query_params.get('job_type', None)
	sort_jobs = request.query_params.get('sort_jobs', None)
	#
	jobs = Jobs.objects.all()
	if location:
		jobs = jobs.filter(location=location)
	if job_type:
		jobs = jobs.filter(job_type=job_type)
	if sort_jobs:
		if sort_jobs == 'ascending':
			jobs = jobs.all().order_by('-posted_on')
		elif sort_jobs == 'descending':
			jobs = jobs.all().order_by('posted_on')
	if jobs:
		serialized = JobsSerializer(jobs, many=True)
		return Response(serialized.data)
	else:
		return Response({})


