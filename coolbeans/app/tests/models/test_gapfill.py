from django.test import TestCase

from coolbeans.app.exceptions import HTMLParseError
from coolbeans.app.models.question import GapFillQuestionModel


class GapFillTestCase(TestCase):
    def test_gap_fill_valid_markup(self):
        """Test gap fill check_html with valid markup"""
        obj = GapFillQuestionModel()
        self.assertTrue(obj.check_html("""This is a <gap answers='["correct", "valid"]' /> gap."""))
        self.assertTrue(obj.check_html("""This is also <gap answers='["a"]' /> <gap answers='["valid", "correct"]'> gap."""))

    def test_gap_fill_invalid_markup(self):
        """Test gap fill check_html with invalid markup"""
        obj = GapFillQuestionModel()
        with self.assertRaises(HTMLParseError):
            obj.check_html("The json parsing will <gap answers=\"fail'\"> on this one")
        with self.assertRaises(HTMLParseError):
            obj.check_html("So will <gap answers=\"{1:3}\"> this one")
