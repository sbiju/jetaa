from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404


from .models import Chat

# Create your views here.


def Home(request):
    chatt = Chat.objects.all()
    return render(request, 'home.html', {'home': 'active', 'chat': chatt })


def Post(request):
    if request.method == 'POST':
        msg = request.POST.get('msgbox', None)
        chatt = Chat(user=request.user, message=msg)
        if msg != "":
            chatt.save()
        return JsonResponse({'msg':msg, 'user': chatt.user.username})
    else:
        return HttpResponse('Request must be a Post')


def Messages(request):
    chatt = Chat.objects.all()
    return render (request,'messages.html', {"chat": chatt})