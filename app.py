from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://thesundarsingh:SundarMongo1234@cluster0.sh84jvm.mongodb.net/?appName=Cluster0")
db = client["testdb"]
collection = db["users"]

# API Route
@app.route('/api')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

# Form Page
@app.route('/todo')
def todo_form():
    return render_template('ToDoForm.html')

# Form Page
@app.route('/')
def form():
    return render_template('form.html')

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return f"Error: {str(e)}"

# To do Form Submission
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        data = request.form
        db.todos.insert_one({
            "itemName": data.get("itemName"),
            "itemDescription": data.get("itemDescription"),
            "itemId": data.get("itemId")
        })
        return redirect(url_for('success'))
    except Exception as e:
        return f"Error: {str(e)}"

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
