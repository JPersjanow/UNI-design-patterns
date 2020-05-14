from flask import Flask, render_template, request, session, redirect, url_for

from ex7_database.db_connect import DB

try:
    from db_connect import DB
    from login import DBLogin
except ModuleNotFoundError:
    from .db_connect import DB
    from .login import DBLogin
import jinja2

app = Flask(__name__)
app.secret_key = b'njujd//adp]a[fpdsvnsi'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect_with_db():
    errors = []
    if request.method == 'POST':
        session['DBNAME'] = request.form['dbname']
        session['PASSWORD'] = request.form['password']
        if DBLogin(dbname=session['DBNAME'], password=session['PASSWORD']).check_password():
            database = DB(db=session['DBNAME'])
            database.connect()
            if database.connection_status == 'SUCCESS':
                database.close_connection()
                return redirect('/lookup_tables')
            else:
                errors.append(database.connection_status)
                database.close_connection()
        else:
            errors.append("Error connecting to the database! Incorrect password")
        return render_template('failure.html', errors=errors)

@app.route('/lookup_tables')
def lookup_tables():
    database = DB(db=session['DBNAME'])
    database.connect()

    if database.connection_status == 'SUCCESS':
        tables = database.get_tables()
        return render_template('show.html', tables=tables)

if __name__ == '__main__':
    app.run(debug=True)
