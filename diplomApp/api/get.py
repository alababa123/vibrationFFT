import json

from rest_framework import status
from diplomApp.models import AccelerationData
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def get_data(request):
    data = json.loads(request.body.decode('utf-8'))

    from_date = data['from']
    to_date = data['to']
    print(AccelerationData.objects.all())
    out = AccelerationData.objects.filter(time__lte=to_date, time__gte=from_date)
    print(out)
    ans = []
    for i in out:
        ans.append({
            'time': i.time,
            'acceleration': i.acceleration
        })

    return Response(status=status.HTTP_200_OK, data=ans)