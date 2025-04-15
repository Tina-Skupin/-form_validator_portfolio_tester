def validate_email(email):
    """
    Validates an email address format.
    
    Args:
        email (str): The email to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    # Basic validation - check for @ symbol and period
    if '@' not in email or '.' not in email:
        return False
        
    # Additional validation logic here
    return True



def main():
    email = "tskupin32@gmail.com"

    Mailokay = validate_email(email)
    print (Mailokay)

if __name__ == "__main__":
    main()