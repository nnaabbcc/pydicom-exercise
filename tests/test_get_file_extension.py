
import unittest

from dicomtest.get_file_extension import get_file_extension

class GetFileExtensionTest(unittest.TestCase):
    def test_get_file_extension_return_e(self):
        self.assertEqual(get_file_extension("a.b.c.e"), ".e")

    def test_get_file_extension_return_xxx_yyy(self):
        ext = get_file_extension('a.b.c.e.xxx_yyy')
        self.assertEqual(ext, '.xxx_yyy')

    def test_get_file_extension_return_empty(self):
        ext = get_file_extension('a_b_c_d_e')
        self.assertEqual(ext, '')
