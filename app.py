from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialisation de la base de données
DATABASE = 'library_db.sqlite'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS Book (
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Author TEXT,
                PublishedYear INTEGER,
                Genre TEXT,
                IsAvailable INTEGER
            )
        ''')
    print("La base de donnee est initialisee.")

@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT * FROM Book")
        books = cursor.fetchall()
    return render_template('index.html', books=books)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("INSERT INTO Book (Title, Author, PublishedYear, Genre, IsAvailable) VALUES (?, ?, ?, ?, ?)",
                         (title, author, year, genre, 1))
        return redirect(url_for('index'))
    return render_template('ajouter.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
 
