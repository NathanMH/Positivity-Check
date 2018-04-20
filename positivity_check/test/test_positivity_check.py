import unittest
import positivity_check

class TestPositivityCheck(unittest.TestCase):
    """ Test Afinn file """
    def test_find_AFINN(self):
        afinn_obj = positivity_check.Afinn()
        self.assertEqual(type(afinn_obj), positivity_check.Afinn)


    """ Test UserText objects """

    def test_with_empty_string(self):
        """ Test with an empty string. """
        test_object = positivity_check.UserText("")
        self.assertTrue(test_object)

    def test_with_gibberish_and_numbers(self):
        """ Test with a nonsense string. """
        test_object = positivity_check.UserText("rneaikkft3 385krnei-r/rnseidkf]")
        self.assertTrue(test_object)

    def test_with_positive_word(self):
        """ Test with a single positive word. """
        test_object = positivity_check.UserText("good")
        self.assertGreater(test_object.pos_count, 0)

    def test_with_positive_capital(self):
        """ Test a positive word with a capital letter. """
        test_object = positivity_check.UserText("Good")
        self.assertGreater(test_object.pos_count, 0)

    def test_with_negative_word(self):
        """ Test with a single negative word. """
        test_object = positivity_check.UserText("hate")
        self.assertGreater(test_object.neg_count, 0)

    def test_with_negative_capital(self):
        """ Test a negative word with a capital letter. """
        test_object = positivity_check.UserText("Hate")
        self.assertGreater(test_object.neg_count, 0)

    def test_word_lists(self):
        """ Test the creation of word lists. """
        test_object = positivity_check.UserText("Hate, love, can't, won't, neutral, none, table, love, great, almost")
        self.assertNotEqual(test_object.word_total, 0)
        self.assertNotEqual(len(test_object.word_list), 0)
        self.assertNotEqual(len(test_object.matching_word_list), 0)

    def test_percentages(self):
        """ Test the math for percentages. """
        test_object = positivity_check.UserText("Hate, love, can't, won't, neutral, none, table, love, great, almost")
        self.assertNotAlmostEqual(test_object.percent_pos, 0)
        self.assertNotAlmostEqual(test_object.percent_neg, 0)
        self.assertNotAlmostEqual(test_object.percent_neutral, 0)

    def test_sentiment(self):
        """ Test the main sentiment property """
        test_object = positivity_check.UserText("Hate, love, can't, won't, neutral, none, table, love, great, almost")
        self.assertNotEqual(test_object.sentiment, 0)

if __name__ == '__main__':
    pass
