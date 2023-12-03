import json

from rest_framework import status
from diplomApp.models import AccelerationData
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def edit_data(request):
    data = json.loads(request.body.decode('utf-8'))
    for i in data['data']:
        AccelerationData(
            time=i['time'],
            acceleration=i['acceleration']
        ).save()
    
    return Response(status=status.HTTP_200_OK, data={
        'ok': True
    })