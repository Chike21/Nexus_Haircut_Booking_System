from django.apps import AppConfig # type: ignore

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        import bookings.signals # for signals (email sending)