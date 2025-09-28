#!/usr/bin/env python3
from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Route for dynamic usernames
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the app only if executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
