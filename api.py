from flask import Flask

# api/:user/repos/
@app.route('/api/<user>/repos')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# api/:user/repos/location/
@app.route('api/<user>/repos/location/')
def show_user_profile(location):
    # show the user profile for that user
    return 'User %s' % username


# api/:user/repos/location/:location
@app.route('api/<user>/repos/location/<location>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# api/:user/repos/category
@app.route('api/<user>/repos/category')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username



# api/:user/repos/category/:category
@app.route('api/<user>/repos/category/<category>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
