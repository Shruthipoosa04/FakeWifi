from django.shortcuts import render

# Create your views here.
from .models import WiFiNetwork

def index(request):
    networks = WiFiNetwork.objects.all().order_by('-timestamp')
    return render(request, 'detection/index.html', {'networks': networks})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WiFiNetwork
from .serializers import WiFiNetworkSerializer

@api_view(['GET', 'POST'])
def wifi_list(request):
    if request.method == 'GET':
        networks = WiFiNetwork.objects.all()
        serializer = WiFiNetworkSerializer(networks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WiFiNetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def index(request):
    query = request.GET.get('query', '')  # Search by SSID or MAC Address
    suspicious_only = request.GET.get('suspicious', '')  # Filter Suspicious

    networks = WiFiNetwork.objects.all().order_by('-timestamp')

    if query:
        networks = networks.filter(ssid__icontains=query) | networks.filter(mac_address__icontains=query)
    
    if suspicious_only:
        networks = networks.filter(is_suspicious=True)

    return render(request, 'detection/index.html', {'networks': networks, 'query': query, 'suspicious_only': suspicious_only})


from django.http import JsonResponse

def check_new_fake_networks(request):
    latest_fake = WiFiNetwork.objects.filter(is_suspicious=True).order_by('-timestamp').first()
    
    if latest_fake:
        return JsonResponse({'new_fake': True, 'ssid': latest_fake.ssid, 'mac_address': latest_fake.mac_address})
    
    return JsonResponse({'new_fake': False})

 

