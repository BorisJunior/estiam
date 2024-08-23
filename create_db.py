import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# Création de la table 'user_messages'
try:
    conn.execute('''
    CREATE TABLE IF NOT EXISTS user_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
    ''')
    print("Table 'user_messages' created successfully")
except Exception as e:
    print(f"An error occurred while creating the 'user_messages' table: {e}")

# Création de la table 'admin_credentials'
try:
    conn.execute('''
    CREATE TABLE IF NOT EXISTS admin_credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    print("Table 'admin_credentials' created successfully")
except Exception as e:
    print(f"An error occurred while creating the 'admin_credentials' table: {e}")

# Commit et fermeture de la connexion
conn.commit()
conn.close()
print("Connection closed successfully")
