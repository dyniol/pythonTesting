import unittest
import rectangle_perimeter
import sys

class TestArea(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 30)

    # @unittest.skipUnless(sys.platform.startswith('win'),
    #      'Requires windows to run test')

    @unittest.skipIf(sys.version_info[0] < 3,
         'Temporarily skips error test')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)

# different syntax for same testcase
#     def test_error(self):
#     self.assertRaises(ValueError, rectangle_perimeter.get_perimeter(10, 0)
    
if __name__ == '__main__':
    unittest.main()