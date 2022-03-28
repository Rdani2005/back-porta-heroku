from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint': 'api/complementarios/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo delas rutas para poder acceder a esta api'
        },
        {
            'endpoint': 'api/desarrollados/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo delas rutas para poder acceder a esta api'
        },
        {
            'endpoint': 'api/enunciados/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo delas rutas para poder acceder a esta api'
        },
        {
            'endpoint': 'api/evaluaciones/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo delas rutas para poder acceder a esta api'
        },
        {
            'endpoint': 'api/indirectas/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo delas rutas para poder acceder a esta api'
        },
        {
            'endpoint': 'admin/',
            'methods': 'GET',
            'body': None,
            'Description': 'Ruta para ingresar como super usuario'
        }

    ]
    return Response(routes)
