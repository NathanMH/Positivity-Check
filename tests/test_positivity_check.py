import unittest
import PositivityCheck

class TestPositivityCheck(unittest.TestCase):
    """ Test PositivityCheck. """

    def test_with_empty_string(self):
        """ Test PositivityCheck with an empty string. """
        test_object = PositivityCheck.UserText("")
        self.assertTrue(test_object)

    def test_with_gibberish_and_numbers(self):
        """ Test with a nonsense string. """
        test_object = PositivityCheck.UserText("rneaikkft3 385krnei-r/rnseidkf]")
        self.assertTrue(test_object)

    def test_with_positive_word(self):
        """ Test with a single positive word. """
        test_object = PositivityCheck.UserText("sweet")
        self.assertGreater(test_object.pos_count, 0)

    def test_with_negative_word(self):
        """ Test with a single negative word. """
        test_object = PositivityCheck.UserText("ass")
        self.assertTrue(test_object)

    def test_with_positive_capital(self):
        """ Test a positive word with a capital letter. """
        test_object = PositivityCheck.UserText("Ass")
        self.assertGreater(test_object.neg_count, 0)

    def test_with_negative_capital(self):
        """ Test a negative word with a capital letter. """
        test_object = PositivityCheck.UserText("Sweet")
        self.assertGreater(test_object.pos_count, 0)

    def test_afinn_file(self):
        self.assertDictEqual()

    def test_set_creation(self):
        """ Test if the set function is functioning. """
        pass
        # test_object = PositivityCheck.UserText(input("Type something damnit!"))
        # print(test_object.afinn.afinn_dict)

if __name__ == '__main__':
    main()
