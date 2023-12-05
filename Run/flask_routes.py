#Author: Brooke Neupert
#Date: 12/3/23
#Purpose: These Flask routes will give a framework for the RecipeVault website

#import statements: 
import prefix

from flask import Flask, url_for, jsonify, redirect
from markupsafe import escape
from flask import render_template
from flask import request
from functions import *

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
	exists, username = get_user(render_template("login.html"))
	if exists:
		return user_vault(username)
	else:
		return render_template("signup.html")

# @app.route('/signup')
# def signup():
# 	exists, username = get_user(render_template("signup.html"))
# 	if exists:
# 		#if user is in db, then redirect to login page
# 		return render_template("login.html")
# 	else:
# 		#create new user and go to empty vault

    
#Vault Page route
@app.route('/user/<username>/my_vault')
def user_vault(username):
	return render_template("vault_page.html")

@app.route('/not_found')
def error404():
	return render_template("404.html")

@app.route('/<recipe_title>/recipe')
def recipe_page(recipe_name):
	return render_template("recipe_pg.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        insert_user(username, password)

        # redirects the user to a home page by using @app.route('/registration-success') 
        return redirect(url_for('registration_success'))

    return render_template('register_page.html')

@app.route('/registration-success')
def registration_success():
    return render_template("home_page.html")

@app.route('/user_info')
def see_users():
    user_info = get_newly_added_user()
    
    # check if user_info is not None before returning
    if user_info:
        # you can modify this based on your actual database schema
        return jsonify({'User Info': user_info})
    else:
        # return response if no user is found
        return jsonify({'message': 'No user found'}), 404
    




# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)