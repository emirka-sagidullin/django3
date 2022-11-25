from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse

# Create your views here.

def posts(request):
    return HttpResponse('Main page')

def new(request):
    return HttpResponse('New posts')

def top(request):
    return HttpResponse('Top posts')

def topComments(request, id):
    if id < 100:
        return HttpResponse(f'Комментариев о товаре: {id}')
    if id > 100:
        return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def newComments(request, id):
    if id < 100:
        return HttpResponse(f'Комментариев о товаре: {id}')
    if id > 100:
        return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def topLikes(request, id):
    if id < 100:
        return HttpResponse(f'Лайков у товара: {id}')
    if id > 100:
        return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def newLikes(request, id):
    if id < 100:
        return HttpResponse(f'Лайков у товара: {id}')
    if id > 100:
        return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def main(request):
    login = request.GET.get("login")
    password = request.GET.get("password")
    return HttpResponse(f"<h2>Login: {login} <br> Password: {password}</h2>")

def about(request):
    return HttpResponseRedirect('/posts')

def contacts(request):
    return HttpResponsePermanentRedirect('/posts/new')

def access(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    if login == 'admin' and password == 'admin':
        return HttpResponse("Все норм")
    else:
        return HttpResponse('Доступ запрещен')

def json(request):
    nm = request.GET.get('name')
    ag = request.GET.get('age')
    Person = {
    'name': nm,
    'age': ag
    }
    return JsonResponse(Person)

def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    response.set_cookie("username", username)
    return response

def get(request):
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")