import hedwig

def signup(phone,carrier):
    lst = [(phone,carrier),]
    receivers = hedwig.receivers(lst)
    code = int(phone) - 1234567890
    msg = "Please enter this code to activate your account   code=>" + str(code)
    hedwig.send(receivers, msg)

    