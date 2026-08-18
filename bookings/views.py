from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date
from .models import Appointment, Service

# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Booking system running")

def home(request):
    return render(request, 'haircut/index.html')

# Signup Logic
def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 1. Check passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # 2. Check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # 3. Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user.save()
        # Automatically log the user in
        login(request, user)

        messages.success(request, "Account created successfully💈Welcome to Nexus HairCut!")
        return redirect("home")

    return render(request, "haircut/signup.html")

# Login Logic
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful 💈")
            return redirect("appointment")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "haircut/login.html")

# Logout Logic
def logout_view(request):
    logout(request)
    return redirect("login")

def about(request):
    return render(request, 'haircut/about.html')

# Booking
@login_required
def appointment(request):

    services = Service.objects.filter(is_active=True)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        booking_date = request.POST.get("date")
        time = request.POST.get("time")
        email = request.POST.get("email")
        service_id = request.POST.get("service")

        # Get selected service
        service = get_object_or_404(
            Service,
            id=service_id,
            is_active=True
        )

        # Convert date and time
        date_obj = datetime.strptime(booking_date, "%Y-%m-%d").date()
        time_obj = datetime.strptime(time, "%H:%M").time()

        # Prevent past dates
        if date_obj < date.today():
            messages.error(
                request,
                "You cannot book a past date."
            )
            return redirect("appointment")

        # Create appointment
        Appointment.objects.create(
            user=request.user,
            service=service,
            name=name,
            phone=phone,
            email=email,
            date=date_obj,
            time=time_obj
        )

        messages.success(
            request,
            "Booking successful 💈"
        )

        return redirect("home")

    services = Service.objects.filter(is_active=True)

    appointments = Appointment.objects.filter(
        user=request.user
    )

    return render(
        request,
        "haircut/appointment.html",
        {
            "appointments": appointments,
            "services": services,
            "today": date.today().isoformat(),
        }
    )

# My Appointments
@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(
        user=request.user
    ).order_by("-date", "-time")

    return render(
        request,
        "haircut/my_appointments.html",
        {
            "appointments": appointments
        }
    )


# Cancel Booking
@login_required
def cancel_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id,
        user=request.user
    )

    if appointment.status != "Pending":
        messages.error(
            request,
            "Only pending appointments can be cancelled."
        )
        return redirect("my_appointments")

    appointment.status = "Cancelled"
    appointment.save()

    messages.success(
        request,
        "Appointment cancelled successfully ❌"
    )
    return redirect("my_appointments")

# Contact
def contact(request):
    return render(request, 'haircut/contact.html')


def open(request):
    return render(request, 'haircut/open.html')


# Price List
def service(request):
    services = Service.objects.all()

    return render(
        request,
        'haircut/service.html',
        {
            'services': services
        }
    )


def team(request):
    return render(request, 'haircut/team.html')


def testimonial(request):
    return render(request, 'haircut/testimonial.html')
