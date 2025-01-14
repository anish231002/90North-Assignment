from django.shortcuts import render
from .models import Message

def chat_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat.html', {'users': users})
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Message

def chat_view(request, username):
    other_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(sender=request.user, receiver=other_user, content=content)
    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages, 'other_user': other_user})
