from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from userprofil.models import UserProfile
from tag.models import Tag

def index(request):
    tag = Tag.objects.all()
    user=request.GET["user"]
    mail_id=request.GET.get("email")
    try:
       mail_id = UserProfile.objects.get(email=mail_id)
       return render(request,'question/enter.html',{
           'user':user,
           'ta':tag,
       })
    except UserProfile.DoesNotExist:
       return render(request, 'userprofil/login.html', {
            'error_message': "login faild enetr a valid entry.",
       })
