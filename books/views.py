from django.shortcuts import render
from django.http import HttpResponse

from book_func import get_user_info

# Create your views here.
def hello(request):
    return HttpResponse('hello, this is douban v2 test page !')

def getuserinfo(request):
    user_id = get_user_info('70276760')
    return HttpResponse('add user %s'%user_id)