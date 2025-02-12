from django.http import HttpResponse
from django.shortcuts import render
from .models import pc
import asyncio

# Create your views here.


def about(request):
    if request.GET:
        print(request.GET)
    return HttpResponse('This is About page')
#http://127.0.0.1:8000/about/?name=Haha&type=other

def home(request):
    return render(request, 'home.html', {'greeting':'Hello!'})

# https://yandex.ru/video/preview/53251734084292116



# https://proproprogs.ru/django4/django4-get-i-post-zaprosy-obrabotchiki-isklyucheniy-zaprosov
# https://metanit.com/python/django/4.7.php
# https://metanit.com/python/django/5.12.php
# https://yourtodo.life/ru/posts/asinhronnyij-django/

# http://127.0.0.1:8000/?hostname=rpc-300&ip=192.168.1.1&user=username

def logi(request):
    print(request.GET)
    #return render(request, 'logi.html')

    # получаем из строки запроса параметры
    hostname = request.GET.get("hostname", "Undefined")
    ip = request.GET.get("ip", "Undefined")
    user = request.GET.getlist("user", ["Undefined"])

    asyncio.run(acreate_person(hostname, ip, user))

    return HttpResponse(f"""
                <div>hostname:   {hostname}</div>
                <div>ip:         {ip}</div>
                <div>users:      {user}</div>
            """)


async def acreate_person(host="nohost", ipa="noip", user="nouser"):
    host = await pc.objects.acreate(hostname=host, ip=ipa, users=user)
    print(host.hostname)
    return


def print(request):
    return HttpResponse()
    # получаем все объекты
    #people = pc.objects.all()
    #print(people.query)
    
    # получаем объекты с именем Tom
    #people = people.filter(name = "rpc-300")
    #print(people.query)
    
    # получаем объекты с возрастом, равным 31
    #people = people.filter(age = 31)
    #print(people.query)
    
    # здесь происходит выполнения запроса в БД
    #for pc in people:
    #    print(f"{pc.id} - {pc.hostname} - {pc.ip} - {pc.users}")