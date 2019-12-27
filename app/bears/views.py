from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "my_text": "The text coming from my views.py",
        "my_number": 789456123,
        "my_list": [223, 565, 88]
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", my_context)
