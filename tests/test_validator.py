import unittest
from src.validator import validate_email, validate_password, validate_name

class TestNameValidator(unittest.TestCase):
    def test_string_name(self):
        """test that name is a string, non-string returns False"""
        self.assertTrue(validate_name("Tina Skupin"))
        self.assertFalse(validate_name(1234))
        self.assertFalse(validate_name(None))

    def test_requirements_name(self):
        """test that requirements are met: at lest one space, at least one upper case letter, at least 5 long, no special characters"""
        "at least one space"
        self.assertFalse(validate_name("Tinaskupin"))
        self.assertFalse(validate_name("Ti s"))
        self.assertTrue(validate_name("Ti sk"))
        self.assertTrue(validate_name("Ti sku"))

    def test_international_names(self):

        # European Name
        self.assertTrue(validate_name("Tina Skupin"))
            # Name with accents
        self.assertTrue(validate_name("José Martínez"))
            # Name with hyphen
        self.assertTrue(validate_name("Jean-Luc Picard"))

        # Russian Name
        self.assertTrue(validate_name("Иван Петров"))

        #special characters
        self.assertFalse(validate_name("Smith&Jones Jones"))


        # Arabic name
        self.assertTrue(validate_name("محمد علي"))

        # Chinese name
        self.assertTrue(validate_name("张伟 张伟"))



"""        

    
    # Mixed script (shouldn't be rejected just because it's unusual)
        self.assertTrue(validate_name("John 张"))
    
    # Still reject special characters
        self.assertFalse(validate_name("李@明"))"""





    

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
        self.assertFalse(validate_email("tinatester.gmail.com"))
    
    def test_invalid_emails2apes(self):
        """Test that valid email formats pass validation, 2 @ """
        result = validate_email("Tskupin2@g@mail.com")
        self.assertEqual(result, False)

    def test_invalid_emails_webadress(self):
        """user submits webadress instead of mailadress"""
        result = validate_email("https.mail@google.commailu0inbox")
        self.assertEqual(result, False)

class TestPasswordValidator(unittest.TestCase):

    def test_string_password(self):
        """test that password is a string, non-string returns False"""
        self.assertFalse(validate_password(123))
        self.assertFalse(validate_password(None))
        self.assertTrue(validate_password("Ineedcoffee1*"))
        self.assertTrue(validate_password("13menonthedeadm*nschesT"))

    def test_requirements_password(self):
        """test that password has at least one number"""
        self.assertFalse(validate_password("coffeewithsugarandmilk"))
        """test that password has at least one uppercase letter"""
        self.assertFalse(validate_password("5coffeewithsugarandmilk"))
        """test that password has at least one lowercase letter"""
        self.assertFalse(validate_password("5COFFEEWITHSUGARANDMILK*"))
        """test that password has at least one star"""
        self.assertFalse(validate_password("5Coffeewithsugarandmilk"))
        """test that password only contains ascii- characters"""
        self.assertFalse(validate_password("5Cöffeewithsugarandmilk*"))
        self.assertFalse(validate_password("5Coffeewithsügarandmilk*"))
        self.assertFalse(validate_password("5Coffeewithsugårandmilk*"))
        

        """test for a valid password"""
        self.assertTrue(validate_password("5Coffeewithsugarandmilk*"))


    def test_length_password(self):
        """test that password has minimum length (10) less returns False"""
        self.assertFalse(validate_password("Coffee1*"))
        self.assertTrue(validate_password("IneedCoffee1*"))

    def test_password_swordfish(self):
        """test that password is not swordfish see https://tvtropes.org/pmwiki/pmwiki.php/Quotes/ThePasswordIsAlwaysSwordfish """
        self.assertFalse(validate_password("Swordfish1"))

    

 
    

if __name__ == '__main__':
    unittest.main()