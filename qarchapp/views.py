from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Information
from .forms import SendForm

def index(request):
    post_list = Post.objects.order_by('id')
    site_info=Information.objects.get(id=1)
    form=SendForm()
    context = { 'post_list': post_list, 'site_info': site_info, 'form':form }

    return render(request, 'qarchapp/index.html', context)


def detail(request, det_id):
    detail = Post.objects.get(pk=det_id)
    site_info=Information.objects.get(id=1)
    context = { 'detail': detail, 'site_info': site_info }

    return render (request, 'qarchapp/detail.html', context)
 