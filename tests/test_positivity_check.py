import unittest
import PositivityCheck

class TestPositivityCheck(unittest.TestCase):
    """
    Test PositivityCheck
    """

    def test_afinn_dictionary(self):
        """
        Test that the AFINN list gets loaded properly
        """
        test_afinn = type(PositivityCheck.AFINN)
        self.assertEqual(test_afinn, dict)

    def test_with_empty_string(self):
        """
        Test PositivityCheck with an empty string
        """
        test_object = PositivityCheck.text_block("")
        test_object.print_stats()

    def test_with_gibberish_and_numbers(self):
        """
        Test with a nonsense string
        """
        test_object = PositivityCheck.text_block("rneaikkft3 385krnei-r/rnseidkf]")
        test_object.print_stats()


if __name__ == '__main__':
    main()
