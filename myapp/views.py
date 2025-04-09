from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Las mejores marcas traídas de todo el mundo"}
    return render(request, "myapp/index.html", context)