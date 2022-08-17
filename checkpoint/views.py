from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
                'questions':[{
                    'question': 'Eres gay?',
                    'options': [
                        'Si soy',
                        'No lo se',
                        'Me declaro cabro',
                        'No'
                    ]
                }],
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
                'questions':[{
                    'question': 'Eres gay?',
                    'options': [
                        'Si soy',
                        'No lo se',
                        'Me declaro cabro',
                        'No'
                    ]
                }],
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
                'questions':[
                    {
                        'question': 'Has bebido alcohol?',
                        'options': [
                            'Si he bebido',
                            'No se ni como me llamo',
                            'No'
                        ]
                    },
                    {
                        'question': 'Tienes un problema mecanico?',
                        'options': [
                            'S',
                            'No estoy seguro',
                            'No'
                        ]
                    },
                ],
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
                'questions':[{
                    'question': 'Eres gay?',
                    'options': [
                        'Si soy',
                        'No lo se',
                        'Me declaro cabro',
                        'No'
                    ]
                }],
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

@api_view(['GET'])
def validate_position(request,lat,lon):
    data = {
        "status": True,
        "description": "El usuario esta dentro.",
        "geofence_name": "ZONA DE CONTROL"
    }
    return Response(data,status=status.HTTP_200_OK)

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        print(request.FILES)
        response = {
            'status':'OK',
            'description':'Information was uploaded successfully.',
        }
        return JsonResponse(response)
    
    response = {
        'status':'error',
        'description':'Get method is not allowed.',
    }
    return JsonResponse(response)