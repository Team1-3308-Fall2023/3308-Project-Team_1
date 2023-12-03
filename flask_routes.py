#Author: Brooke Neupert
#Date: 12/3/23
#Purpose: These Flask routes will give a framework for the RecipeVault website

#import statements: 
import prefix

from flask import Flask, url_for
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

prefix.use_PrefixMiddleware(app)


#Gets URL When run in csel.io virtual machine
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

#default (Home Page)
@app.route('/')
def home_route():
	return render_template("home_page.html")

#Search Page route
@app.route('/search')
def search_route():
	return render_template("search_page.html")

#Login Page:
@app.route('/login')
def login():
	exists, username=get_user(render_template("login.html"))
	if exists:
		return user_vault(username)
	else:
		return render_template("signup.html")
	
#Vault Page route
@app.route('/user/<username>/my_vault')
def user_vault(username):
	return render_template("vault_page.html")

@app.route('/not_found')
def error404():
	return render_template("404.html")

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)