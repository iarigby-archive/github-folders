# github-folders
call with `python github-folders.py`
### parameters:
#### `clone`
Makes it easy to organize your repositories, and transfer setup between machines. gets all your repos, if you have `folder-<foldername>` in topics, it will clone it under `<rootDirectory>/<foldername>.`

#### `create-repo`
Creates a new github repository from current directory, adds it as remote, runs `push --set-upstream` (yeah I'm that lazy)

## TODO 
- check if folder already there
- run git fetch
- parameter to get all the folders and their contents currently
- user can specify pattern for folder naming
- handle git log in and stuff, maybe generate ssh keys (since it's a new computer)
- store my auth token somewhere (and add it to .gitignore)
- instead of topic, providing structure in description could be better, like user/group/etc

additional points in google doc
## quick links
[github api](https://developer.github.com/v3/)
