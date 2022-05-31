from flask import Flask
from flask_mongoengine import MongoEngine

database_name = 'blogDatabase'
password = '9849559082'
DB_URI = f'mongodb+srv://laxmanMaharjan:{password}@cluster17.dadlw.mongodb.net/{database_name}?retryWrites=true&w=majority'

app = Flask(__name__)

@app.route('/')
def index():
    return "api is working"

@app.route('/hello')
def index1():
    return "hello world"

DATABASE ={
        'host':DB_URI,
        'connect':False
        }


app.config["MONGODB_SETTINGS"]=DATABASE
# app.config["MONGODB_HOST"]=DB_URI

db = MongoEngine(app)

from crudApp.views import crud_blueprint
app.register_blueprint(crud_blueprint)
