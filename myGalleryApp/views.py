from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {"aristote":images})

def search_results(request):

    if 'search_image' in request.GET and request.GET["search_image"]:
        search_term = request.GET.get("search_image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

