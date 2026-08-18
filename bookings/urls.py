from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path("my_appointments/", views.my_appointments, name="my_appointments"),
    path(
    "cancel/<int:id>/",
    views.cancel_appointment,
    name="cancel_appointment"
),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout",),
    path('open/', views.open, name='open'),
    # path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]
