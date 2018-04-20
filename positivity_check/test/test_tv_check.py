import unittest
import os

import tv_check

csv_test_loc = os.getcwd() + "\\positivity_check\\test\\the-office-lines-scripts-test.csv" # Windows
characters_test = ["Michael", "Jim"]

class TestFuncs(unittest.TestCase):
    """ Test tv script analyzer """

    def test_load_csv(self):
        """ Test loading csv file """
        tv_check.load_csv(csv_test_loc)
        self.assertEqual(type(), 0)

class TestClasses(unittest.TestCase):
    """ Test classes """

    def test_character_init(self):
        jason = tv_check.Character("Jason")
        self.assertEqual(jason.name, "Jason")
    
    def test_character_add_text(self):
        jason = tv_check.Character("Jason")
        jason.add_text(1, 2, "Test line text.")
        self.assertGreater(len(jason.seasons), 0)
        self.assertGreater(len(jason.episodes), 0)
        self.assertEqual(jason.total_text, "Test line text. ")

    def test_season(self):
        second = tv_check.Season(2)
        second.add_text( "Test line text.")
        self.assertEqual(second.total_text, "Test line text. ")

    def test_episode(self):
        third = tv_check.Episode(3)
        third.add_text("Test line text.")
        self.assertEqual(third.total_text, "Test line text. ")

    def test_scene(self):
        fourth = tv_check.Scene(4)
        fourth.add_text("Test line text.")
        self.assertEqual(fourth.total_text, "Test line text. ")


if __name__ == '__main__':
    unittest.main()
