"""enter mailadress for testing the code here
email = "tina.skupin@gmail.com" """

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
    return True



def main():

    Mailokay = validate_email(email)
    print (Mailokay)

if __name__ == "__main__":
    main()