import sqlite3

def insert_user(username, password):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()

    # using placeholders to prevent SQL injection
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    conn.commit()
    conn.close()

    

def get_newly_added_user():
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()

    # retrieve usernames and passwords of newly added users
    c.execute('''
        SELECT username, password
        FROM users;
    ''')

    result = c.fetchall()
    conn.close()
    return result
    

def search_recipes_by_query(query):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()
	# '''
	# Fetches recipes based on user input 'query' 
	# Usage case would probably built around implementing a form element into the search_page.html file and utilizing 'POST' methods to send the data
	# --html--
	# <form action="/search" method="POST">
	# 	<input type="text" name="query" placeholder="Search...">
	# 	<input type="submit" value="Search">
	# </form>
	# --python--
	# query = request.form.get('query')
	# # insert this in the search route?
	# if request method is POST
	# 	query = request.form.get('query')
	# 	recipes = search_by_query(query)
	# 	do something to render recipes
	# '''
    # Query to select recipes based on their names or related keywords
    c.execute('''
        SELECT * FROM recipes
        WHERE recipeName LIKE ? OR ingredients LIKE ? OR directions LIKE ?
	''', ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    
    recipes = c.fetchall()
    conn.close()
    return recipes


def add_recipe_to_vault(user_id, recipe_id):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()

    # Insert the user ID and recipe ID into the savedRecipes table to represent the recipe being saved by the user
    c.execute('INSERT INTO savedRecipes (userID, recipeID) VALUES (?, ?)', (user_id, recipe_id))

    conn.commit()
    conn.close()
    
def retrieve_comments(recipe_id):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()
    
    c.execute(
        '''SELECT comment, event_datetime 
        FROM comments 
        WHERE recipeID = ?
        ORDER BY event_datetime''', 
        (recipe_id,))
    
    recipe_comments = c.fetchall()
    
    conn.commit()
    conn.close()   
    
    return recipe_comments

def retrieve_recipe(recipe_id):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()
    
    c.execute(
        '''SELECT recipeName, ingredients, directions, averageRating
        FROM recipes 
        WHERE id = ?''', 
        (recipe_id,))
    
    recipe_info = c.fetchall()
    
    conn.commit()
    conn.close()   
    
    return recipe_info

def check_credentials(username, password):
    conn = sqlite3.connect('recipeDB.db')
    c = conn.cursor()
    # SELECT query to check credentials
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))

    # fetch the result
    result = c.fetchone()
    c.close()

    # check if the result is not None (means credentials are valid)
    return result is not None


    
if __name__ == "__main__":
    # Example usage:
    # insert_user('Linnea', 'password62')
    new_user_info = get_newly_added_user()
    print("Users Info:", new_user_info)
    
    