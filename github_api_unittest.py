import unittest
import github_api

class TestApiController(unittest.TestCase):

    def test_parsing(self):
        parsed = github_api.match_github_description(
            {'description': 'abcd location:home category:personal'},
            github_api.location_regex)
        self.assertEqual(parsed, 'home', 'should extract the tag correctly')
        
        
if __name__ == '__main__':
    unittest.main()
