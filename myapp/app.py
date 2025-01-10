from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    collection.insert_one({'name': name, 'email': email})
    return 'User added successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

