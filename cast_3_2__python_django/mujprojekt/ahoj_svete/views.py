from django.shortcuts import render


def index(request):
    return render(request, 'ahoj_svete/index.html')
