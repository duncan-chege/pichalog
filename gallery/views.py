from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def display_images(request):
    return render(request, 'display_images.html')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        
        return render(request, "search.html",{"images": searched_images})       #articles is a key while searched_images is a value
