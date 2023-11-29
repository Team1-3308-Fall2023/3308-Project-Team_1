import sqlite3

#Initialize the database and create the 'users' table if it doesn't exist
#Run once to initalize starting tables

conn = sqlite3.connect('recipeDB.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );''')

c.execute('''
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoryName VARCHAR(255) NOT NULL
    );''')

c.execute('''
    CREATE TABLE userDietaryPreferences (
        userID INT NOT NULL,
        categoryID INT NOT NULL,
        FOREIGN KEY (userID) REFERENCES users(id),
        FOREIGN KEY (categoryID) REFERENCES categories(id)
    );''')

c.execute('''
    CREATE TABLE recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipeName VARCHAR(255) NOT NULL,
        ingredients VARCHAR(255) NOT NULL,
        directions VARCHAR(255) NOT NULL,
        averageRating FLOAT
    );''')

c.execute('''
    CREATE TABLE recipeCategories (
        recipeID INT NOT NULL,
        categoryID INT NOT NULL,
        FOREIGN KEY (recipeID) REFERENCES recipes(id),
        FOREIGN KEY (categoryID) REFERENCES categories(id)
    );''')

c.execute('''
    CREATE TABLE comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment VARCHAR(255) NOT NULL,
        event_datetime DATETIME,
        userID INT NOT NULL,
        recipeID INT NOT NULL,
        FOREIGN KEY (userID) REFERENCES users(id),
        FOREIGN KEY (recipeID) REFERENCES recipes(id)
    );''')

c.execute('''
    CREATE TABLE savedRecipes (
        userID INT NOT NULL,
        recipeID INT NOT NULL,
        FOREIGN KEY (userID) REFERENCES users(id),
        FOREIGN KEY (recipeID) REFERENCES recipes(id)
    );''')
    
c.execute('''
    CREATE TABLE ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rating INT CHECK (rating >= 1 AND rating <= 5),
        userID INT NOT NULL,
        recipeID INT NOT NULL,
        FOREIGN KEY (userID) REFERENCES users(id),
        FOREIGN KEY (recipeID) REFERENCES recipes(id)
    );''')


#Insert data

test_accounts = [
    ('testuser1', 'password1'),
    ('testuser2', 'password2')
 ]
test_categories = [
    ('breakfast',),
    ('lunch',),
    ('dinner',),
    ('vegetarian',),
]


test_recipes = [
    ('breakfastRecipe1', 'breakfastRecipeIngredients1', 'breakfastRecipeDirections1'),
    ('breakfastRecipe2', 'breakfastRecipeIngredients2', 'breakfastRecipeDirections2'),
    ('breakfastRecipe3', 'breakfastRecipeIngredients3', 'breakfastRecipeDirections3'),
    ('lunchRecipe1', 'lunchRecipeIngredients1', 'lunchRecipeDirections1'),
    ('lunchRecipe2', 'lunchRecipeIngredients2', 'lunchRecipeDirections2'),
    ('lunchRecipe3', 'lunchRecipeIngredients3', 'lunchRecipeDirections3'),
    ('dinnerRecipe1', 'dinnerRecipeIngredients1', 'dinnerRecipeDirections1'),
    ('dinnerRecipe2', 'dinnerRecipeIngredients2', 'dinnerRecipeDirections2'),
    ('dinnerRecipe3', 'dinnerRecipeIngredients3', 'dinnerRecipeDirections3'),
    ('vegitarianRecipe1', 'vegitarianIngredients1', 'vegitarianRecipeDirections1'),
    ('vegitarianRecipe2', 'vegitarianIngredients2', 'vegitarianRecipeDirections2'),
    ('vegitarianRecipe3', 'vegitarianIngredients3', 'vegitarianRecipeDirections3')
    
    
]



c.executemany('INSERT INTO users (username, password) VALUES (?, ?)', test_accounts)

c.executemany('INSERT INTO categories (categoryName) VALUES (?)', test_categories)

c.executemany('INSERT INTO recipes (recipeName, ingredients, directions) VALUES (?, ?, ?)', test_recipes)

#Insert testing

# c.execute('SELECT * FROM users')
# user_actual = c.fetchall()

# print("users_actual:")
# for row in user_actual:
#     print(row)
    
# c.execute('SELECT * FROM categories')
# category_actual = c.fetchall()

# print("category_actual:")
# for row in category_actual:
#     print(row)
    
# c.execute('SELECT * FROM recipes')
# recipe_actual = c.fetchall()

# print("recipe_actual:")
# for row in recipe_actual:
#     print(row)

conn.commit()
conn.close()