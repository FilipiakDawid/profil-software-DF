import unittest
import ReadJsonFile


class TestReadJsonFile(unittest.TestCase):

    def setUp(self):
        self.local_file = "persons.json"
        self.api_url = "https://randomuser.me/api/"

    def test_read_file_from_api(self):
        result = ReadJsonFile.read_file_from_api(self.api_url)
        result2 = ReadJsonFile.read_file_from_api(self.api_url, 25)
        result3 = ReadJsonFile.read_file_from_api(self.api_url, '25')

        self.assertEqual(result['info']['results'], len(result['results']))
        self.assertEqual(result2['info']['results'], len(result2['results']))
        self.assertEqual(result3['info']['results'], len(result3['results']))

    def test_read_file_local(self):
        result = ReadJsonFile.read_file_local(self.local_file)
        self.assertNotEqual(result, None)


if __name__ == '__main__':
    unittest.main()