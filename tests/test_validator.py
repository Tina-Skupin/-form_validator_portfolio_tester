import unittest
from src.validator import validate_email

class TestEmailValidator(unittest.TestCase):
    
    def test_valid_emails(self):
        """Test that valid email formats pass validation"""
        result = validate_email("tskupin@gmail.com")
        self.assertEqual(result, True)

    def test_valid_emails2(self):
        """should pass, number"""
        result = validate_email("tskupin2@gmail.com")
        self.assertEqual(result, True)

    def test_valid_emails3(self):
        """should pass validation, uppercase"""
        result = validate_email("Tskupin2@gmail.com")
        self.assertEqual(result, True)

    def test_valid_emailsUmlaut(self):
        """should pass validation, Umlaut"""
        result = validate_email("Tsküpin2@gmail.com")
        self.assertEqual(result, True)

    def test_valid_emailsnotstring(self):
        """You shall not pass- test- not a string (number)"""
        result = validate_email(213)
        self.assertEqual(result, False)
    
    def test_valid_emails2apes(self):
        """Test that valid email formats pass validation, 2 @ """
        """this is not a valid mail and should not work!"""
        result = validate_email("Tskupin2@g@mail.com")
        self.assertEqual(result, True)

    def test_valid_emails_space(self):
        """You shall not pass- test- space"""
        result = validate_email("Tskupin 2@g@mail.com")
        self.assertEqual(result, False)

    def test_valid_emails_subdomain(self):
        """should pass validation - subdomain"""
        result = validate_email("tina@skupin.example.de")
        self.assertEqual(result, True)

    def test_valid_emails_plussign(self):
        """should pass validation - plus"""
        result = validate_email("tina+tester@example.com")
        self.assertEqual(result, True)

    

if __name__ == '__main__':
    unittest.main()