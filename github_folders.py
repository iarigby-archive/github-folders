import requests
import json
import re
import os
import subprocess
import sys

root_directory = "~/pythontest"
user = 'iarigby'
headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
regex = re.compile(r'folder-([a-zA-Z0-9-]*)')
github_api = 'https://api.github.com'

if len(sys.argv) > 1:
        auth_token = sys.argv[1]
        print(auth_token)
        headers["Authorization"] = f'token {auth_token}'

def has_valid_length(folders, name):
    if len(folders) > 1:
        print(f'multiple folders specified for {name}')
        return False
    elif len(folders) == 0:
        print(f'no folder specified for {name}, skipping')
        return False
    else:
        print(f'cloning {name}...')
        return True

def create_and_cd_dir(directory):
    if 'root' in directory:
        dir = os.path.expanduser(root_directory)
    else:
        dir = os.path.expanduser(f'{root_directory}/{directory}')
        if not os.path.exists(dir):
            os.makedirs(dir)
    os.chdir(dir)

def get_github_link(repo_name, user=user):
    return f'{github_api}/repos/{user}/{repo_name}'

def get_github_repo(repo_name, user=user):
    return f'git@github.com:{user}/{repo_name}'

def clone_repos():    
    r = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers)
    for j in r.json():
        repo_name = j["name"]
        req = requests.get(f"{get_github_link(repo_name)}/topics", headers=headers)
        topics = req.json()['names']
        folders = list(filter(regex.match, topics))
        if has_valid_length(folders, repo_name):
            directory = regex.search(folders[0]).group(1)
            create_and_cd_dir(directory)
            subprocess.call(f'git clone {get_github_repo(repo_name)}', shell=True)

## TODO ssh response include ssh clone url

def create_repo():
    pwd = os.getcwd()
    dir_name = pwd[pwd.rfind('/') + 1 : len(pwd)]
    repo = {'name': dir_name}
    r = requests.post(f'{github_api}/user/repos', data=json.dumps(repo), headers=headers, auth=(input('user: '), input('password: ')))
    # git_url = r.json()['ssh_url']
    # print(git_url)
    if True: #git_url:
        subprocess.call('git status', shell=True)
        subprocess.call(f'git remote add origin {get_github_repo(dir_name)} && git push origin master', shell=True)
    git_url = r.json()['ssh_url']
    print(git_url)
    
if (__name__=='__main__'):
    if 'clone' in sys.argv:
        clone_repos()
    elif 'newrepo' in sys.argv:
        create_repo()
    else:
        print('no valid action')