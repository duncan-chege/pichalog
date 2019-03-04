from django.shortcuts import render
from .models import Image

# Create your views here.
def initial(request):
        all_images = Image.objects.all()
        return render(request, 'search.html',{"all_images":all_images})

def search_results(request):
        if 'searchCategory' in request.GET and request.GET["searchCategory"]:
                search_term = request.GET.get("searchCategory")
                searched_images = Image.search_by_category(search_term)
                message= f"Showing: {search_term} pictures"
                
                return render(request, 'search.html' , {"message":message, "all_images": searched_images})       #images is a key while searched_images is a value

        else:
                message = "You haven't searched for anything"
                return render(request, 'search.html' , {"message":message}) 


                

                
        


