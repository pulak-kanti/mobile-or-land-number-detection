# The program will work only for valid phone number with and without country code

def remove_extra_char(phone_number):
    new_number = ""
    for char in phone_number:
        if char.isdigit() or char is '+':
            new_number+=char
    return new_number


def getExtensionNo(country, phone_number):
    if phone_number[0] is not '+':
        return None
    first_chars = phone_number[0:3]
    return first_chars
    

def isMobile(country, phone_number):
    phone_number = remove_extra_char(phone_number)
    country_code = getExtensionNo(country,phone_number)
    if country_code:
        phone_number = phone_number[3:]
    if country is "NL":
        if phone_number[0:2] == "06":
            return True
        else:
            return False
        
    if country is 'BE':
        if phone_number[0:2] == "04":
            return True
        else:
            return False

    if country is 'IT':
        if phone_number[0] == '3':
            return True
        else:
            return False
        
    if country is 'ES':
        if phone_number[0] == '6' or ( phone_number[0] == '7' and phone_number[1] !='0') :
            return True
        else:
            return False
    
    if country is 'GB' or country is 'UK':
        if phone_number[0:2] == '07':
            return True
        else:
            return False

    if country is 'FR':
        if phone_number[0:2] == '06' or phone_number[0:2] == '07':
            return True
        else:
            return False
    
    if country is 'DE':
        prefix_list = ['20','31','40','42','4911','50','53','60','61','71','81','91']
        for prefix in prefix_list:
            if prefix == phone_number[0:2] or prefix == phone_number[0:4]:
                return True
        return False
        

if  __name__ == "__main__":
    print(isMobile("ES","67134340"))


