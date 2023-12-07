from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from .models import Usuario
from .serializers import UsuarioSerializer
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse
from api.utils.utils import load_model

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Visualizar Usuarios': '/listarUsuarios',
        'Criar Usuario': '/criarUsuario',
        'Atualizar Usuario': '/atualizar/<pk>/',
        'Deletar Usuario': '/usuario/<pk>/deletar/'
    }
    return Response(api_urls)

@extend_schema(request=UsuarioSerializer)
@api_view(['POST'])
def add_user(request):
    user_serializer = UsuarioSerializer(data=request.data)

    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UsuarioSerializer)
@api_view(['GET'])
def view_users(request):
    if request.query_params:
        users = Usuario.objects.filter(**request.query_params.dict())
    else:
        users = Usuario.objects.all()

    if users:
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@extend_schema(request=UsuarioSerializer)
@api_view(['POST'])
def update_users(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    serializer = UsuarioSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=UsuarioSerializer)
@api_view(['DELETE'])
def delete_users(request, pk):
     user = get_object_or_404(Usuario, pk=pk)
     user.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)

     previsao
@api_view(['GET'])
def fazer_previsao(request, id_dado):
    model = load_model()
    dado = get_object_or_404(Usuario, pk=id_dado)
    dados_preprocessados = UsuarioSerializer(dado).data

    try:
        previsao = model.predict([dados_preprocessados])
        response_data = {'previsao': previsao.tolist()}
    except Exception as e:
        response_data = {'erro': str(e)}

    return JsonResponse(response_data)
