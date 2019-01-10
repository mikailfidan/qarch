from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Information, Message
from .forms import SendForm

def index(request):
    post_list = Post.objects.order_by('id')
    message_list = Message.objects.all()
    site_info=Information.objects.get(id=1)
    form=SendForm()
    context = { 'post_list': post_list, 'site_info': site_info, 'form':form, ' message_list': message_list }

    return render(request, 'qarchapp/index.html', context)


def detail(request, det_id):
    detail = Post.objects.get(pk=det_id)
    site_info=Information.objects.get(id=1)
    context = { 'detail': detail, 'site_info': site_info }

    return render (request, 'qarchapp/detail.html', context)
 
def sendmessage(request):
    form = SendForm()
    post_list = Post.objects.order_by('id')
    site_info=Information.objects.get(id=1)
       
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, message=message)

    context = {
        'post_list': post_list, 'site_info': site_info, 'form':form  
    }     
   
    
    
    return render(request, 'qarchapp/index.html', context)