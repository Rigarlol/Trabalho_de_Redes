from rest_framework import viewsets
from jogos.api import serializers
from jogos import models
from rest_framework.response import Response
from rest_framework import status

class JogoViewSet(viewsets.ModelViewSet):
    queryset = models.Jogo.objects.all()
    serializer_class = serializers.JogoSerializer

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        headers = {'X-My-Header': 'my-value'}
        return Response({'message': 'HTTP GET endpoint'}, status=status.HTTP_200_OK, headers=headers)

    def post(self, request, *args, **kwargs):
        token = "token-ficticio"
        if algum_erro_ocorreu:
            return Response({'message': 'Erro ocorreu', 'Authorization': token}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({'message': 'HTTP POST endpoint', 'Authorization': token}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        return Response({'message': 'HTTP PUT endpoint'}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        return Response({'message': 'HTTP DELETE endpoint'}, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        return Response({'message': 'HTTP PATCH endpoint'}, status=status.HTTP_200_OK)

    def options(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        return Response({
            'message': 'HTTP OPTIONS endpoint',
            'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']
        }, status=status.HTTP_200_OK)

    def head(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        return Response(status=status.HTTP_200_OK)