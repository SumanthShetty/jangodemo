from django.shortcuts import render
from django.http import HttpResponse
from userprofil.models import UserProfile
from question.models import Question
from tag.models import Tag
def index(request):
    user=request.user
    
    question_title=request.GET["q_title"]
    question_body=request.GET["q_body"]
    tag=request.GET["tag"]
    tg=Tag.objects.get(id=int(tag))
    print tg
    point=request.GET["points"]
    
    #c,created=Question.objects.update_or_create(user=user, question_title=question_title, question_body=question_body, point=point)
    #c.tag.add(tg)
    #c.save()
    #question = Question.objects.all()
    return render(request,'answer/display.html')
