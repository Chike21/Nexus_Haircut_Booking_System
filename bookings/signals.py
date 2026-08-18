from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Appointment
from django.core.mail import send_mail

@receiver(pre_save, sender=Appointment)
def appointment_status_change(sender, instance, **kwargs):
    if instance.pk:
        old = Appointment.objects.get(pk=instance.pk)

        if old.status != instance.status:
            send_mail(
                subject="Appointment Update 💈",
                message=f"Your appointment is now {instance.status}",
                from_email="chikezirimjustice@gmail.com",
                recipient_list=[instance.email],
                fail_silently=True,
            )