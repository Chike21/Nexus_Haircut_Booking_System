from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Appointment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
    Service,
    on_delete=models.PROTECT,
    null=True,
    blank=True
)

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    date = models.DateField()

    time = models.TimeField()

    email = models.EmailField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.name} | {self.service} | {self.date}"