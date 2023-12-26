from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def dashboard(r):
    print("hello")
    return render(r, "dashboard/index.html")
