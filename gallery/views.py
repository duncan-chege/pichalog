from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def display_images(request):
    return render(request, 'display_images.html')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = 