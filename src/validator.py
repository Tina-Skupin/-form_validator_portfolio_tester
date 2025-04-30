"""enter mailadress for testing the code here"""
email = "tina.skupin@gmail.com"
password = 42

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
    
    if len(password)< 11:
        print ("Password too short")
        return False
    
    if ' ' in password:
        print ("password must not contain spaces")
        return False

    print ("Password: is valid")
    return True

def validate_email(email):
    """
    Validates an email address format.
    
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



def main():

    Mailokay = validate_email(email)
    print (Mailokay)

    Passwordokay = validate_password(password)
    print (Passwordokay)

if __name__ == "__main__":
    main()