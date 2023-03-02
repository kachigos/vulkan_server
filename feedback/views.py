from rest_framework.response import Response
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests


class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data

        message_text = "New message:\n"
        for key, value in data.items():
            if key in ["username", "phone", 'email', 'country', 'subject', 'desc']:
                message_text += f"{key}: {value}\n"

        chat_id = "956591994"
        bot_token = "5877156981:AAH5_hfQW5CG8JH2K04iphPEe5cEe78GQvU"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}
        requests.post(url, json=payload)

        return response



@receiver(post_save, sender=Feedback)
def feedback(instance, *args, **kwargs):
    send_contact(
        f"ФИО: {instance.username}"
        f"\nEmail: {instance.email}"
        f"\nНомер: {instance.phone}"
        f"\nСтрана: {instance.country}"
        f"\nТема: {instance.subject}"
        f"\nТекст: {instance.desc}"
    )


def send_contact(data):

    to_email = 'chyngyzsubhanov@gmail.com'
    send_mail(
        'Subject',
        f'{data}',
        'from@example.com',
        [to_email],
        fail_silently=False
    )
