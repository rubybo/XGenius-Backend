import openai as openai
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from .models import Chat

openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    answer = response.choices[0].message.content.strip()
    return answer


# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat/chatbot.html', {'chats': chats})
