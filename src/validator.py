import unicodedata

"""enter mailadress for testing the code here"""
email = "tina.skupin@gmail.com"
password = "HIPPOPOTAMUSINTHEHOLe42*"
name = "Tina Skupin"

def validate_name(name):
    """ validates Name format.
    Args: name (str): the name to validate
    Return bool: True if valid, False otherwise
    """
    if not isinstance(name, str):
        print ("not a string")
        return False
    
    if not ' ' in name:
        print ("Name must at least be 2 words (first name, last name)")
        return False
    
    if any(char.isdigit() for char in name):
        print ("Name cannot contain numbers")
        return False
    
    """if not any(char.isupper() for char in name):
        print ("name must at least contain one upper case letter")
        return False"""

    if len(name) < 5:
        print ("name must be at least 5 or more long")
        return False


    """international names are allowed, no other speical signa except hyphens"""
    for char in name:
        # Check if character is a letter in any language, a space, or hyphen
        category = unicodedata.category(char)
        # L* covers all letter categories (Lu, Ll, Lt, Lo, etc.)
        if not (category.startswith('L') or char.isspace() or char == '-'):
            print("Name can only contain letters, spaces, and hyphens")
            return False

    print ("Name: is valid")
    return True


def validate_email(email):
    """ Validates an email address format.
    Args:
        email (str): The email to validate
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(email, str):
        print ("not a string")
        return False
    
    # Basic validation - check for @ symbol and period
    if '@' not in email or '.' not in email:
        print ("@ or . missing")
        return False
    
    if ' ' in email:
        print ("adress contains spaces")
        return False
    
    if len(email) > 100:
        print ("maximum length (100)")
        return False
        
    if email.count('@') != 1:
        print ("more than one @")
        return False
    
    if "www" in email or "http" in email:
        print ("this is a webadress, not a mailadress")
        return False

    # Additional validation logic here
    print ("Email: is valid")
    return True

def validate_password(password):
    """
    Validates an password format.
    args:
        password(str): the password to validate
        
    Returns: 
        bool True if valif, False otherwise"""
    if not isinstance(password, str):
        print ("not a string")
        return False
    
    "password must at least contain one number"
    if not any(char.isdigit() for char in password):
        print ("password must contain at least one number")
        return False
    
    if not any(char.isupper() for char in password):
        print ("password must at least contain one upper case letter")
        return False
    
    if not any(char.islower() for char in password):
        print ("password must at least contain one lower case letter")
        return False
    
    if not '*' in password:
        print ("PAsswordmustcontain a star")
        return False
    
    if not all(char.isascii() for char in password):
        print("Password must only contain ASCII characters (no Ä, ö, ü, etc.)")
        return False

    if len(password)< 11:
        print ("Password too short")
        return False
    
    if ' ' in password:
        print ("password must not contain spaces")
        return False
    
    if 'Swordfish' in password:
        print ("password must not contain Swordfish, for further information ask Commander Vimes")

    print ("Password: is valid")
    return True

def main():

    Nameokay = validate_name(name)
    print (Nameokay)

    Mailokay = validate_email(email)
    print (Mailokay)

    Passwordokay = validate_password(password)
    print (Passwordokay)

if __name__ == "__main__":
    main()
