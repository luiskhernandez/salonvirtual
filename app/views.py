from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def home(request):
    if request.user.is_authenticated():
        return redirect(reverse("dashboard"))
    return render_to_response("home.html",locals(),RequestContext(request))

@login_required(login_url="/login")
def dashboard(request):
    return render_to_response("dashboard.html",locals(),RequestContext(request))

def logout_(request):
    logout(request)
    return redirect(reverse("home"))


