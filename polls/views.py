from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world")


def hello(request):
    return HttpResponse("Try to print hello")
