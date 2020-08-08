import unittest
import os


class Data_Base(unittest.TestCase):

    def setUp(self):
        self.database_name = "profilSoftwareDF.db"

    def test_database_file_exist(self):
        self.assertEqual(os.path.isfile(self.database_name), True)


if __name__ == '__main__':
    unittest.main()
