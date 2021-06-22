import os
import random
from wsgiref.util import FileWrapper

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView,
from FortAPI.settings import MEDIA_ROOT, REQUEST_URL
from api.models import Table
import time


@api_view(['GET'])
def get_file(request, path):
    file_path = MEDIA_ROOT + "/" + path
    file = open(file_path, 'rb')
    res = HttpResponse(
        file.read(),
        content_type='application/png'
    )
    res['Content-Disposition'] = 'filename=' + os.path.basename(file_path)
    return res


@api_view(['POST'])
def post(request):
    tag = request.data['tag']
    type = request.data['type']
    data = Table.objects.filter(type=type, disabled=False)
    result = []
    for i in data:
        if tag in i.tags.split(','):
            result.append(i)

    if len(result) == 1:
        item = result[0]
        return JsonResponse({'type': type, 'tag': tag, 'link': f'{REQUEST_URL}api/file/{item.file.name}'})
    if len(result) > 1:
        index = random.randint(0, len(result))
        item = result[index - 1]
        return JsonResponse({'type': type, 'tag': tag, 'link': f'{REQUEST_URL}api/file/{item.file.name}'})

    return Response({'error': 'no_results'})
