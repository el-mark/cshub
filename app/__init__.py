from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '37a05ef5242d150aa1bb6088332db0db'

from app import views