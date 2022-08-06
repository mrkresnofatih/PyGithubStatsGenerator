import unittest
from dateutils import get_latest_date_strings_list
from dateutils import get_custom_date_string

class TestDateUtils(unittest.TestCase):
    def test_get_latest_date_strings_list_should_return_non_empty_list(self):
        result = get_latest_date_strings_list()
        self.assertTrue(len(result) > 0)
    
    def test_get_custom_date_string_should_return_non_empty_string(self):
        datestringinput = "2022-07-23"
        result = get_custom_date_string(datestringinput)
        expected = "220723"
        self.assertEqual(result, expected)
    
    def test_get_latest_date_strings_list_should_return_10_members(self):
        result = get_latest_date_strings_list()
        self.assertTrue(len(result) == 10)

if __name__ == '__main__':
    unittest.main()