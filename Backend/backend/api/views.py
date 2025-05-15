from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RealEstateDataSerializer
from .models import RealEstateData

# Create your views here.


@api_view(['GET'])
def analyze_location(request, location):
    data = RealEstateData.objects.filter(location__iexact=location)
    if not data.exists():
        return Response({"error": "Location not found"}, status=404)
    
    serializer = RealEstateDataSerializer(data, many=True)
    return Response({
        "location": location,
        "data": serializer.data
    })