from django.http import HttpResponse

def home(request):
    # request.method
    # request.get_full_path()
    return HttpResponse("<h1>hello world</h1>")

