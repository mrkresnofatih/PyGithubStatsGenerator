import unittest
from colorutils import get_random_color_palette

class TestColorUtils(unittest.TestCase):
    def test_get_random_color_palette_should_return_10_member_list(self):
        result = get_random_color_palette()
        self.assertTrue(len(result) == 10)

if __name__ == '__main__':
    unittest.main()