"""
server.py

This module sets up a Flask web application with several routes to demonstrate 
basic functionality such as returning JSON responses, handling errors, and 
searching for names in a predefined list.
"""

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
    """Return a hello world message."""
    return "hello world"

@app.route("/no_content")
def no_content():
    """Return 'no content found' with a status of 204.

    Returns:
        tuple: A tuple containing a dictionary with the message and a status code of 204.
    """
    return {"message": "No content found"}, 204

@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200.

    Returns:
        tuple: A tuple containing a dictionary with the message and a status code of 200.
    """
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp

@app.route("/name_search")
def name_search():
    """Find a person in the database.

    Returns:
        dict: The person if found, with status of 200.
        tuple: A dictionary with an error message and a status of 404 if not found.
        tuple: A dictionary with an error message and a status of 422 if the 'q' parameter is missing.
    """
    data = [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Jane", "last_name": "Smith"},
        {"first_name": "Alice", "last_name": "Johnson"}
    ]

    query = request.args.get("q")

    if not query:
        return {"message": "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    return {"message": "Person not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
