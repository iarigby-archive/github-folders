import unittest
import github_api
import cache

class TestApiController(unittest.TestCase):
    
    def test_get_user_repos(self):
        print(github_api.get_user_repos('iarigby'))
        
    def test_parsing(self):
        parsed = github_api.match_github_description(
            {'description': 'abcd location:home category:personal'},
            github_api.location_regex)
        self.assertEqual(parsed, 'home', 'should extract the tag correctly')

        
    def test_parse_descriptions(self):
        print("*** categories ***")
        repos_category =github_api.parse_descriptions(cache.get(), github_api.category_regex) 
        for tag in repos_category:
            print('\t' + tag) 
            for repo in repos_category[tag]:
                print(repo['name'] + ':' + repo['url'])
        print("*** locations ***")
        location_repos = github_api.parse_descriptions(cache.get(), github_api.location_regex)
        for tag in location_repos:
            print('\t' + tag) 
            for repo in location_repos[tag]:
                print(repo['name'] + ':' + repo['url'])
                
if __name__ == '__main__':
    unittest.main()
