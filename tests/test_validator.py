import unittest
from src.validator import validate_email, validate_password

class TestPasswordValidator(unittest.TestCase):

    def test_string_password(self):
        """test that password is a string, non-string returns False"""
        self.assertFalse(validate_password(123))
        self.assertFalse(validate_password(None))
        self.assertTrue(validate_password("Ineedcoffee1*"))
        self.assertTrue(validate_password("13menonthedeadm*nschesT"))

    def test_length_password(self):
        """test that password has minimum length (10) less returns False"""
        self.assertFalse(validate_password("Coffee1*"))
        self.assertTrue(validate_password("IneedCoffee1*"))

    

    

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

    def test_invalid_emails_maxlength(self):
        """should not pass validation - max-length"""
        result = validate_email("GalliaestomnisdivisainpartestresquarumunamincoluntBelgaealiamAquitanitertiamquiipsorumlinguaCeltaenostraGalliappellantur@cesar.com")
        self.assertEqual(result, False)

    def test_invalid_emails_no_ape(self):
        """should not pass validation - no @ sign"""
        result = validate_email("tinatester.gmail.com")
        self.assertFalse(result)
    
    def test_invalid_emails2apes(self):
        """Test that valid email formats pass validation, 2 @ """
        result = validate_email("Tskupin2@g@mail.com")
        self.assertEqual(result, False)

    def test_invalid_emails_webadress(self):
        """user submits webadress instead of mailadress"""
        result = validate_email("https.mail@google.commailu0inbox")
        self.assertEqual(result, False)

    

if __name__ == '__main__':
    unittest.main()