# Development

install flask
## run
`FLASK_APP=apy.py`
`python -m flask run`

## test
`python github_api_unittest.py`


# Description
This project will help categorize github repositories by including predefined tags in the description. Sometimes it's better to not clone all repositories in one folder, and you would like to preserve the setup accross. You can try out example links to see how it works

## Usage
The user will update the repository description with tags, for example `location:home`, `category:school`

## Endpoints

##### api/healthCheck
returns ok to let us know that it is up and running

##### api/:user/repos/
returns the list ordered by create date
example: `http://127.0.0.1:5000/api/iarigby/repos`

##### api/:user/repos/location/
returns the list of all repos sorted by location. 
example: `http://127.0.0.1:5000/api/iarigby/repos/location`
eg I want this repository to be synced on my work laptop but not home laptop.

##### api/:user/repos/location/:location
returns the list of all repos which have a location tag "location"
example: `http://127.0.0.1:5000/api/iarigby/repos/location/home`

##### api/:user/repos/category
returns the list of all repos sorted by category, for example personal projects, school projects, etc
example: `http://127.0.0.1:5000/api/iarigby/repos/category`
##### api/:user/repos/category/:category

example: `http://127.0.0.1:5000/api/iarigby/repos/category/documents`

 
