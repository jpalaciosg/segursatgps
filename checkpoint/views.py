from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_control_sets(request):
    try:
        data = [
            {
                'id':1,
                'name':'CONTROL GRIFOS',
                'description':'CONTROL DE ABASTECIMIENTO EN GRIFOS',
                'pictures':[
                    {
                        'name': 'Selfie',
                        'description': 'El coductor debe tomarse una foto'
                    },
                    {
                        'name': 'Placa',
                        'description': 'Placa del vehiculo'
                    }
                ]
            },
            {
                'id':2,
                'name':'CONTROL PERNOCTE',
                'description':'CONTROL EN ZONAS DE PERNOCTE',
                'pictures':[
                    {
                        'name': 'Selfie',
                        'description': 'El coductor debe tomarse una foto'
                    },
                    {
                        'name': 'Placa',
                        'description': 'Placa del vehiculo'
                    }
                ]
            },
        ]
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'detail':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_control_set(request,id):
    try:
        data = [
            {
                'id':1,
                'name':'CONTROL GRIFOS',
                'description':'CONTROL DE ABASTECIMIENTO EN GRIFOS',
                'pictures':[
                    {
                        'name': 'Selfie',
                        'description': 'El coductor debe tomarse una foto'
                    },
                    {
                        'name': 'Placa',
                        'description': 'Placa del vehiculo'
                    }
                ]
            },
            {
                'id':2,
                'name':'CONTROL PERNOCTE',
                'description':'CONTROL EN ZONAS DE PERNOCTE',
                'pictures':[
                    {
                        'name': 'Selfie',
                        'description': 'El coductor debe tomarse una foto'
                    },
                    {
                        'name': 'Placa',
                        'description': 'Placa del vehiculo'
                    }
                ]
            },
        ]
        return Response(data[id-1],status=status.HTTP_200_OK)
    except Exception as e:
        error = {'detail':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)