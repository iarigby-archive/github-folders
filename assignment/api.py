import github_api
from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def root():
    return 'see README.md for api endpoints'

@app.route('/api/healthCheck')
def health_check():
    return 'OK'

# api/:user/repos/
@app.route('/api/<user>/repos')
def show_user_repos(user):
    #returns the list of repos: name, description, url
    return jsonify(github_api.get_user_repos(user))


# api/:user/repos/location/
@app.route('/api/<user>/repos/location/')
def show_user_repos_by_location(user):
    #returns the list of all repos sorted by location.
    return jsonify(github_api.get_user_repos_by_tag(user, 'location'))


# api/:user/repos/location/:location
@app.route('/api/<user>/repos/location/<location>')
def show_user_repos_for_location(user, location):
    #returns the list of all repos which have a location tag "location"
    repos = github_api.get_user_repos_by_tag(user, 'location')
    if location in repos:
        return jsonify(repos[location])
    else:
        return 'none'

# api/:user/repos/category
@app.route('/api/<user>/repos/category')
def show_user_repos_by_category(user):
    #returns the list of all repos sorted by category
    # for example personal projects, school projects, etc
    return jsonify(github_api.get_user_repos_by_tag(user, 'category'))

# api/:user/repos/category/:category
@app.route('/api/<user>/repos/category/<category>')
def show_user_repos_for_category(user, category):
    # returns the list of all repos which have a category tag "category"
    repos = github_api.get_user_repos_by_tag(user, 'category')
    if category in repos:
        return jsonify(repos[category])
    else:
        return 'none'
