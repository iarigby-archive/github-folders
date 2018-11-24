import requests
import json
import re
import os
import subprocess
import sys

root_directory = "~/pythontest"
user = 'iarigby'
headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
if len(sys.argv) > 1:
    auth_token = sys.argv[1]
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

regex = re.compile(r'folder-([a-zA-Z0-9-]*)')
r = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers)
for j in r.json():
    repo_name = j["name"]
    req = requests.get(f"https://api.github.com/repos/{user}/{repo_name}/topics", headers=headers)
    topics = req.json()['names']
    folders = list(filter(regex.match, topics))
    if has_valid_length(folders, repo_name):
        directory = regex.search(folders[0]).group(1)
        create_and_cd_dir(directory)
        subprocess.call(f'git clone git@github.com:{user}/{repo_name}', shell=True)
    
    