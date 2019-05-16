from flask import Flask

# api/:user/repos/
@app.route('/api/<user>/repos')
def show_user_repos(user):
    #returns the list ordered by create date
    return 'User %s' % user


# api/:user/repos/location/
@app.route('api/<user>/repos/location/')
def show_user_repos_by_location(user):
    #returns the list of all repos sorted by location.
    return 'User %s' % user


# api/:user/repos/location/:location
@app.route('api/<user>/repos/location/<location>')
def show_user_repos_for_location(user, location):
    #returns the list of all repos which have a location tag "location"
    return 'User %s' % user

# api/:user/repos/category
@app.route('api/<user>/repos/category')
def show_user_repos_by_category(user):
    #returns the list of all repos sorted by category
    # for example personal projects, school projects, etc
    return 'User %s' % user



# api/:user/repos/category/:category
@app.route('api/<user>/repos/category/<category>')
def show_user_repos_for_category(user, category):
    # returns the list of all repos which have a category tag "category"
    return 'User %s' % user
