#Author: Brooke Neupert
#Date: 12/3/23
#Purpose: These Flask routes will give a framework for the RecipeVault website

#import statements: 
import prefix

from flask import Flask, url_for, jsonify, redirect, session, render_template
from markupsafe import escape
from flask import render_template
from flask import request
from functions import *

app = Flask(__name__)
app.secret_key = 'asdfghjkl'

prefix.use_PrefixMiddleware(app)


#Gets URL When run in csel.io virtual machine
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

#default (Home Page)
@app.route('/home')
def home():
    username = session.get('username')  # retrieve username from the session
    return render_template("home_page.html", username=username)
	# return render_template("home_page.html")

#Search Page route
@app.route('/search', methods=['GET','POST'])
def search_route():
	if request.method == 'POST':
         # extracts value from search field
        keyword = request.form['keyword']
        
        recipe_list = search_recipes_by_query(keyword)
        
        return render_template('search_results.html', recipes=recipe_list, search_term=keyword)
        
    else:
        return render_template("search_page.html")
    

#Login Page:
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
     # extracts values of the username and password fields from the form data submitted by the user
        username = request.form['username']
        password = request.form['password']

        # if login is successful, store username in session
        if check_credentials(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login_page.html', error='Invalid credentials')
    else:
        return render_template('login_page.html')
#ORIGINAL
	# exists, username = get_user(render_template("login.html"))
	# if exists:
	# 	return user_vault(username)
	# else:
	# 	return render_template("signup.html")
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('/login'))

# ROUTE WAS UNFINISHED
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

@app.route('/recipes/<recipe_title>/<int:recipe_id>')
def recipe_page(recipe_id):

    recipe_info = retrieve_recipe(recipe_id)

    comms = retrieve_comments(recipe_id)

    #added comms argument so it can be accessed in the recipe_pg.html page using jinja templating syntax
    return render_template("recipe-pg.html", comms=comms) 


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

@app.route('/users')
def users():
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