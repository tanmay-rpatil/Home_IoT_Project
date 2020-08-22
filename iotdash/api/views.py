from django.http import HttpResponse, JsonResponse
from .models import LatestData
# Create your views here.
def index(request):
	count = LatestData.objects.all().count()
	data = list(LatestData.objects.all().values()[count-7:]) #get last 7 entries to generate a graph
	#print(type(data))
	return JsonResponse(data, safe=False)
	
