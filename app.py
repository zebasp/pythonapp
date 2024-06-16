from flask import Flask

app = Flask(__name__)  # Create a Flask application instance

@app.route('/')  # Defines a route for the root URL (/)
def hello():
    return 'Hello, World!'  # Function to handle the request and return a response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 