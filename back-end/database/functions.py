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
        SELECT id
        FROM users
        ORDER BY id DESC
        LIMIT 1;
    ''')

    result = c.fetchone()
    conn.close()
    return result
    


if __name__ == "__main__":
    # Example usage:
    insert_user('Linnea', 'password623')
    new_user_info = get_newly_added_user()
    print("Users Info:", new_user_info)
    
    