import pymysql
from flask import *
from unknown.blueprints.win01_page import win01_page

app = Flask(__name__)

app.register_blueprint(win01_page)

@app.route('/')
def home():
    return render_template('')