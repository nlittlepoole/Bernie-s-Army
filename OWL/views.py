from django.shortcuts import render
from OWL.models import Soldier
import datetime
def index(request):
    #query = request.GET.get('q', '')
    #query = "HN" if query=='' else query
    #print validate(query)
    #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
    #context_dict = {'boldmessage': query + ":",'urls':urls}
    context_dict = {}
    return render(request, 'index.html', context_dict)
    
def signup(request):
    print request.POST
    phone  = request.POST.get("phone","")
    zip_code = request.POST.get("zip_code",0)
    carrier = request.POST.get("carrier","")
    
    print phone,zip_code,carrier
    
    private = Soldier(phone=phone, zip_code=zip_code, carrier=carrier, join_date = datetime.datetime.now())
    private.save()
    #query = "HN" if query=='' else query
    #print validate(query)
    #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
    #context_dict = {'boldmessage': query + ":",'urls':urls}
    context_dict = {}
    return render(request, 'index.html', context_dict)
# Create your views here.
