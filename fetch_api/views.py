# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from fetch_api.utils import (
    count_nodes,
    fetch_nodes,
)

class GetNodesCount(APIView):
    def get(self, request):
        count_info = {
            'node_type': request.GET.get('t', 'Protein'),
            'text': request.GET.get('q', ''),
        }
        count = count_nodes(count_info)
        data = {
            'response': {
                'status': '200',
                'data': count,
            },
        }
        return Response(data)

        # return Response('Temporary Data', status=status.HTTP_200_OK)
class GetNodesData(APIView):
    def get(self, request):
        fetch_info = {
            'node_type': request.GET.get('t', 'Protein'),
            'search_text': request.GET.get('q', ''),
            'limit': 10,
            'page': int(request.GET.get('p', 1)),
        }
        nodes = fetch_nodes(fetch_info)
        data = {
            'response': {
                'status': '200',
                'rows':len(nodes),
                'data': nodes,
            },
        }
        return Response(data)
class GetNodeData(APIView):
    def get(self, request):
        return Response('Temporary Data', status=status.HTTP_200_OK)
