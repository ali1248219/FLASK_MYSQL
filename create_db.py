from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy()
db.init_app(app)

if __name__ == "__main__":
    app.run()