from django.shortcuts import render
from django.http import JsonResponse
from .models import Log
from django.db.models import Max

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")

def aboutus(request):
    return render(request, "frontend/aboutus.html")

def chart(request):
    maxp = Log.objects.all().aggregate(Max("points"))
    pointList = Log.objects.all().order_by('date')
    ctx = {'maxp': maxp["points__max"], "pointList": pointList}
    return render(request, "frontend/chart.html", ctx)

def log(request):
    # Data
    latest_logs = list(Log.objects.order_by('date')[:5].values())

    # Json Response
    return JsonResponse(latest_logs,safe=False)