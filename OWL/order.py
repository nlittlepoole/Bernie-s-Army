import hedwig
from OWL.models import Soldier

def signup(phone,carrier):
    lst = [(phone,carrier),]
    receivers = hedwig.receivers(lst)
    code = int(phone) - 1234567890
    msg = "Please enter this code to activate your account   code=>" + str(code)
    hedwig.send(receivers, msg)

def all_send(msg):
    soldiers = Soldier.objects.filter(active=1)
    lst = [(x.phone,x.carrier) for x in soldiers]
    receivers = hedwig.receivers(lst)
    hedwig.send(receivers, msg) 
    
def zip_send(zips, msg):
    soldiers = Soldier.objects.filter(active=1,zip_code__in=zips)
    
    lst = [(x.phone,x.carrier) for x in soldiers]
    receivers = hedwig.receivers(lst)


    hedwig.send(receivers, msg)

    