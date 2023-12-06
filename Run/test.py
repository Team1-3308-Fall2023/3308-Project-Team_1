# c.execute('SELECT * FROM recipes')
# recipe_actual = c.fetchall()

# print("recipe_actual:")
# for row in recipe_actual:
#     print(row)

conn.commit()
conn.close()