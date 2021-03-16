from finalsa import Services, Webhook

token = "YkhWcGN6SXhPRFEzT0RVMU9ERXdPVFF4TmpVMk56TXlOdz09"
#services = Services("http://192.168.1.113:5001", token)
services = Services("http://0.0.0.0:5001", token)

device_token  = "0289704490f24ef01366b7efd5e2588c7f17a6f77574f5626eb45e428a32723e"
def test_apn():
    topic = "com.finalsa.Server-Managment"
    r = services.send_apn( topic, {
            "alert" : {
                "title" : "Alerta",
                "subtitle" : "prubea",
                "body" : "dsjndsijnfidsnfindsifnijsdnfidsnufinsduifnsuidf"
            },
            "sound" : "default",
            "badge" : 1
        }, device_token,)
    print(r)
    r = services.send_apn(topic, {
            "alert" : {
                "title" : "Alerta",
                "subtitle" : "prubea",
                "body" : "dsjndsijnfidsnfindsifnijsdnfidsnufinsduifnsuidf"
            },
            "sound" : "default",
            "badge" : 1
        }, 
        device_token,
        hook= Webhook('http://localsdsdk:5001', '', { 'sadasd' :'ad'})
    )
    print(r)

def test_calixta():
    r = services.send_calixta_sms(
        "5543670621",
        "hola"
    )
    print(r)

def test_recharge():
    r = services.single_recharge(
        "INT5", "5543670621", 
    )
    print(r)

def test_email():
    r = services.send_email(
        'Luis<luis@finalsa.com>', "luisjimenez6245@hotmail.com",
        "prueba", "holaaa", content = [
            {
                'text' : '<html><body><b>aaaa</b></body></html>'
            }
        ]
    )
    print(r)


test_email()