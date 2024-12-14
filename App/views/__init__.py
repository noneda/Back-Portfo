from rest_framework.decorators import api_view
#* from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def root(req):
    return Response(
        {
            'ProjectName' : 'FullRestApi for Portfolio',
            'author' : 'noneda',
            'others' : '... ? Idk'
        },
        status= status.HTTP_200_OK
    )


