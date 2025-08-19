from django.shortcuts import render

from .models import Message


# Create your views here.
def index(request):
    return render(request, "index.html")

def api(request):
    if request.method == "POST":
        content = request.POST.get("message")
        if content and content.strip() != "":
            message = Message(content=content)
            message.save()

    messages = Message.objects.order_by('-datetime')
    return render(request, "api.html", {
        "messages": messages
    })
