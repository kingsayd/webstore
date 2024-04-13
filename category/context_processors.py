
from .models import Category

def menu_links(request):
    #we will fetch all category list hear 
    links =Category.objects.all()
    return dict(links=links)        # brin all category list and store it in varible links and can use it 