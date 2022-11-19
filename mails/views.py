from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import MailList
from .serializers import MailListSerializer,UpdateMailListSerializer

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def mail_list_view(request):
    # verificar privilegios
    if privilege.view_mail_lists(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    mail_lists = MailList.objects.filter(account=request.user.profile.account)
    for mail_list in mail_lists:
        try:
            mail_list.created = gmt_conversor.convert_utctolocaltime(mail_list.created)
            mail_list.modified = gmt_conversor.convert_utctolocaltime(mail_list.modified)
        except Exception as e:
            print(e)
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    return render(request,'mails/mail-lists.html',{
        'mail_lists':mail_lists,
        'navbar':navbar,
    })

@api_view(['GET'])
def get_mail_lists(request):
    try:
        mail_lists = MailList.objects.filter(account=request.user.profile.account)
        serializer = MailListSerializer(mail_lists,many=True)
        data = serializer.data
        for i in range(len(data)):
            mail_list = data[i]['mails'].split(',')
            mail_list = [x.replace(' ','') for x in mail_list]
            data[i]['email_number'] = len(mail_list)
            del data[i]['account']
            data[i]['created'] = gmt_conversor.convert_utctolocaltime(mail_lists[i].created)
            data[i]['modified'] = gmt_conversor.convert_utctolocaltime(mail_lists[i].modified)
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_mail_list(request,id):
    try:
        mail_list = MailList.objects.get(id=id,account=request.user.profile.account)
        serializer = MailListSerializer(mail_list,many=False)
        data = serializer.data
        mails = data['mails'].split(',')
        mails = [x.replace(' ','') for x in mails]
        data['email_number'] = len(mails)
        del data['account']
        data['created'] = gmt_conversor.convert_utctolocaltime(mail_list.created)
        data['modified'] = gmt_conversor.convert_utctolocaltime(mail_list.modified)
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_mail_list(request):
    data = request.data
    try:
        data['account'] = request.user.profile.account.id
    except Exception as e:
        error = {
            'detail': 'Account does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = MailListSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_mail_list(request,id):
    data = request.data
    try:
        mail_list = MailList.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': "Mail list does not exist."
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateMailListSerializer(mail_list,data=data)
    if serializer.is_valid():
        mail_list.name = data['name']
        mail_list.description = data['description']
        mail_list.mails = data['mails']
        mail_list.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_mail_list(request,id):
    try:
        mail_list = MailList.objects.get(id=id,account=request.user.profile.account)
        mail_list.delete()
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)