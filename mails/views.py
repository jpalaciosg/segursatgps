from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import MailList
from .serializers import MailListSerializer

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def mail_list_view(request):
    """
    # verificar privilegios
    if privilege.view_latest_alerts(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    """
    mail_lists = MailList.objects.filter(account=request.user.profile.account)
    for mail_list in mail_lists:
        try:
            mail_list.created = gmt_conversor.convert_localtimetoutc(mail_list.created)
            mail_list.modified = gmt_conversor.convert_localtimetoutc(mail_list.modified)
        except Exception as e:
            print(e)
    return render(request,'mails/mail-lists.html',{
        'mail_lists': mail_lists,
    })

@api_view(['GET'])
def get_mail_list(request,id):
    try:
        mail_list = MailList.objects.get(id=id,account=request.user.profile.account)
        serializer = MailListSerializer(mail_list,many=False)
        data = serializer.data
        #data['mails'] = data['mails'].replace(' ','').split(';')
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
