from django.shortcuts import render
from datetime import datetime

def home(request):
    now = datetime.now()

    if now.hour < 12:
        greeting = "Good morning"
    elif now.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    context = {
        "name": "Ashlie",
        "today": now,
        "greeting": greeting,
        "items": ["Microwave", "Steam Mode", "Presets"],
    }

    return render(request, "home.html", context)