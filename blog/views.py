from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import Http404
from .models import Articles


def blog_home(request):
    a = Articles.objects.all()
    context = {
        'name': 'javad',
        'data': a
    }
    
    return render(request, "blog/home.html", context)

def blog_page(request):

    return HttpResponse("hello world111111111111111111111")

def pade_detail(request, page_id):
    a = get_object_or_404(Articles, id=page_id)
    return HttpResponse(a)
    # try:
    #     a = Articles.objects.get(id=page_id)
    #     return HttpResponse(a)
    # except Articles.DoesNotExist:
    #     raise Http404("Article Does not found ...")



