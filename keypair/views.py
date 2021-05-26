from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from .models import KeyPair
from .serializers import KeySerializer


@api_view(['POST', ])
def generate_uuid(request):
    if request.method == 'POST':
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            key_pair = KeyPair.objects.all().order_by('-key').values()
            data = []
            for i in key_pair:
                key = i['key']
                pair = i['uuid']
                k = '{0} : {1}'.format(key, pair)
                data.append(k)
            json_data = JSONRenderer().render(data)
            return Response(json_data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)