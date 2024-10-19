from django.shortcuts import render


# Create your views here.
def render_home_page(request):
    return render(template_name = "core_app/home.html", request = request )

def render_registration_page(request):
    return render(template_name = "core_app/registration.html", request = request )

def render_login_page(request):
    return render(template_name = "core_app/login.html", request = request )
