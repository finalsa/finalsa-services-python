from finalsa import Services

services = Services("http://0.0.0.0:5001", 'YkhWcGN6SXhPRFEzT0RVMU9ERXdPVFF4TmpVMk56TXlOdz09')

def test_apn():
    r = services.send_apn("com.finalsa.Server-Managment", {
            "alert" : {
                "title" : "Alerta",
                "subtitle" : "prubea",
                "body" : "dsjndsijnfidsnfindsifnijsdnfidsnufinsduifnsuidf"
            },
            "sound" : "default",
            "badge" : 1
        }, "0289704490f24ef01366b7efd5e2588c7f17a6f77574f5626eb45e428a32723e",)
    print(r)

def test_calixta():
    r = services.send_calixta_sms(
        "5543670621",
        "hola"
    )
    print(r)



test_calixta()