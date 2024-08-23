from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

# Page d'accueil utilisateur avec le formulaire de contact
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user_messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            con.commit()

        return redirect(url_for('confirmation'))

    return render_template('index.html')


# Page de confirmation d'envoi de message
@app.route("/confirmation")
def confirmation():
    return render_template('confirmation.html')


# Page de login administrateur
@app.route("/login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM admin_credentials WHERE username = ? AND password = ?", (username, password))
            admin = cur.fetchone()

            if admin:
                session['admin'] = True
                return redirect(url_for('admin_home'))
            else:
                return render_template('admin_login.html', error="Invalid credentials")

    return render_template('admin_login.html')


# Page d'accueil administrateur avec la liste des demandes utilisateurs
@app.route("/admin")
def admin_home():
    if 'admin' in session:
        con = sqlite3.connect('database.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM user_messages")
        rows = cur.fetchall()
        con.close()
        return render_template('admin_home.html', rows=rows)
    else:
        return redirect(url_for('admin_login'))


# Route pour déconnecter l'administrateur
@app.route("/admin/logout")
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))


if __name__ == "__main__":
    app.run(debug=True)
