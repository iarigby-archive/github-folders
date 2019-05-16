# Development

install flask
## run
`FLASK_APP=apy.py`
`python -m flask run`

## test
`python github_api_unittest.py`


# Description
This project will help categorize github repositories by including predefined tags in the description. Sometimes it's better to not clone all repositories in one folder, and you would like to preserve the setup accross

## Usage
The user will update the repository description with tags, for example `location:home`, `category:school`

# Tasks

## 1. Endpoints

##### api/healthCheck
returns ok to let us know that it is up and running

##### api/:user/repos/
returns the list ordered by create date

##### api/:user/repos/location/
returns the list of all repos sorted by location. 

eg I want this repository to be synced on my work laptop but not home laptop.

Possible values are:
- `:location` any value from the user
- `all` means that the repo should be synced to all possible `:string` values

##### api/:user/repos/location/:location
returns the list of all repos which have a location tag "location"

##### api/:user/repos/category
returns the list of all repos sorted by category, for example personal projects, school projects, etc

##### api/:user/repos/category/:category


## 2. Setup
After getting all the user repos, we need to parse description for pattern

### Files
Not sure if names are good, suggest new ones if you want

#### API.py
set up flask and list all the endpoints

#### github.py
Functions
- get all repos of the user from github and filter values we're interested in (repo name, url, description...)
- parse the descriptions and add them to json object (category, location values)
- functions that filter and sort that object


## 3. Postman
TODO
 
