import requests
import re
import cache

github_api = 'https://api.github.com'
headers = {'Accept': 'application/vnd.github.mercy-preview+json'}

default_locations = ['untagged', 'all']
default_categories = ['untagged']

def get_github_link(repo_name, user):
    return f'{github_api}/repos/{user}/{repo_name}'

# re.search(r'([a-zA-Z0-9-]*)', get_github_link).group()
location_regex = re.compile(r'location:([a-zA-Z0-9-]*)')
category_regex = re.compile(r'category:([a-zA-Z0-9-]*)')

print(category_regex)

def match_github_description(reply_json, regex):
    #return regex.search(reply_json['description'])
    description = reply_json['description']
    if description:
        tag = regex.search(reply_json['description'])
        if tag:
            return tag.group(1)
        else:
            return 'none'
    else: 
        return 'none'

def get_repo_info(repo):
    return {
        'name': repo['name'],
        'description': repo['description'],
        'url': repo['url']
}

def get_user_repos(user):
    # repos = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers).json()
    repos = cache.get()
    # return list(map(lambda x: x['description'], repos))
    # return parse_descriptions(repos)
    return list(map(lambda x: get_repo_info(x), repos))
    # for j in r.json():
      #   repo_name = j["name"]
       #  req = requests.get(f"{get_github_link(repo_name)}/topics", headers=headers)

# tag type can be location or cateogry
def parse_descriptions(repos, regex_type):
    categorized_repos = {}
    for repo in repos:
        tag = match_github_description(repo, regex_type)
        if tag in categorized_repos:
            categorized_repos[tag].append(repo)
        else:
            categorized_repos[tag] = [repo]
    #return list(map(lambda x: match_github_description(x, regex_type), repos))
    return categorized_repos
# compdef 

def get_user_repos_by_tag(user, tag):
    if tag is 'location':
        repos = parse_descriptions(get_user_repos(user), location_regex)
    elif tag is 'category':
        repos = parse_descriptions(get_user_repos(user), category_regex)
    return repos
