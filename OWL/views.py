from django.shortcuts import render
from OWL.models import Soldier
import datetime
import order
def index(request):
    #query = request.GET.get('q', '')
    #query = "HN" if query=='' else query
    #print validate(query)
    #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
    #context_dict = {'boldmessage': query + ":",'urls':urls}
    context_dict = {}
    if request.mobile:
        return render(request, 'mobile-index.html', context_dict)
    else:
        return render(request, 'index.html', context_dict)
    
def signup(request):
    phone  = request.POST.get("phone","")
    phone = filter( lambda x: x in '0123456789.', phone )
    zip_code = request.POST.get("zip_code",0)
    carrier = request.POST.get("carrier","")
    
    private = Soldier(phone=phone, zip_code=zip_code, carrier=carrier, join_date = datetime.datetime.now())
    private.save()
    order.signup(phone,carrier)
    #query = "HN" if query=='' else query
    #print validate(query)
    #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
    #context_dict = {'boldmessage': query + ":",'urls':urls}
    context_dict = {}
    return render(request, 'code.html', context_dict)

def activate(request):
    code  = request.POST.get("code","")
    phone = str(int(code) + 1234567890)
    if Soldier.objects.filter(phone=phone).count() == 0:
        context_dict = {"fail":True}
        return render(request, 'code.html', context_dict)
    else:
        
        private = Soldier.objects.filter(phone=phone)[0]
        private.active = 1
        private.save()
        #query = "HN" if query=='' else query
        #print validate(query)
        #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
        #context_dict = {'boldmessage': query + ":",'urls':urls}
        context_dict = {}
        return render(request, 'success.html', context_dict)
# Create your views here.
def command(request):
    #query = request.GET.get('q', '')
    #query = "HN" if query=='' else query
    #print validate(query)
    #urls = tweets.search_for_links(query) if not validate(query) else tweets.adjacent_links(query)
    #context_dict = {'boldmessage': query + ":",'urls':urls}
    context_dict = {}
    return render(request, 'command.html', context_dict)