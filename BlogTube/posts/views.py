from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("mainpage")



def group_post(request):
    return HttpResponse('list of posts')


def group_post_detail(request, pk):
    return HttpResponse(f'Post number {pk}')