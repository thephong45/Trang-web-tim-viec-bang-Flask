from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()
python = c.execute(
    '''SELECT * FROM fami WHERE label="Python" ''').fetchall()
command = c.execute(
    '''SELECT * FROM fami WHERE label="Command" ''').fetchall()
sysadmin = c.execute(
    '''SELECT * FROM fami WHERE label="sysadmin" ''').fetchall()
lastest = c.execute(
    '''SELECT * FROM fami WHERE label="Lastest" ''').fetchall()


@app.route('/')
def template():
    return render_template('home.html', python=python,
                           command=command, sysadmin=sysadmin,
                           lastest=lastest)


if __name__ == "__main__":
    app.run(debug=True)
