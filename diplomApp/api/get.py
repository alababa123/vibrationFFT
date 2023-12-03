import json
import numpy as np
from rest_framework import status
from diplomApp.models import AccelerationData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scipy.fft import fft


@api_view(['POST'])
def get_data(request):
    data = json.loads(request.body.decode('utf-8'))

    from_date = data['from']
    to_date = data['to']
    print(AccelerationData.objects.all())
    out = AccelerationData.objects.filter(time__lte=to_date, time__gte=from_date)
    n = len(out)

    acceleration = [i.acceleration for i in out]

    dt = from_date - to_date   
    freq = np.fft.fftfreq(n, dt)
    fft_values = fft(acceleration)
    magnitude_spectrum = list(np.abs(fft_values))
    print(magnitude_spectrum)   

    return Response(status=status.HTTP_200_OK)