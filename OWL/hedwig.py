import smtplib

def receivers(pairs):
    mapping = {
        "Sprint":"@messaging.sprintpcs.com",
        "AT&T":"@txt.att.net",
        "T-Mobile":"@tmomail.net",
        "Verizon":"@vtext.com",
        "US Cellular": "@email.uscc.net",
        "Virgin Mobile": "@vmobl.com",
        "Boost": "@myboostmobile.com",
        "Cricket":"@sms.mycricket.com",
        "Metro PCS": "@mymetropcs.com",
        }
    result = []
    for phone,carrier in pairs:
        result.append(phone+mapping.get(carrier))
    return result

def send(soldiers,msg):
    print soldiers, msg
    soldiers.append("berniesrevolution@gmail.com")
    sender = 'berniesrevolution@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login("berniesrevolution@gmail.com","D4rkc0c04")
        server.sendmail(sender, soldiers, msg)
        server.quit()        
        print "Successfully sent email"
    except Exception as e:
        print e
        print "Fuck"