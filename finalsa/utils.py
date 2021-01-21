def verify_phone(phone):
    res = ''
    if(len(phone) == 10):
        res += '+52' + phone
    return res