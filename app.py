from flask import Flask, render_template

# Create a Flask application instance
# __name__ tells Flask where to look for resources like templates and static files
app = Flask(__name__)

# Define a route for the homepage ("/")
@app.route('/')
def home():
    """
    This function handles requests to the homepage.
    It renders the index.html template.
    """
    # The render_template function looks inside the 'templates' folder
    # for the specified HTML file.
    return render_template('index.html')

# This block ensures the server only runs when the script is executed directly
# (not when imported as a module)
if __name__ == '__main__':
    # Run the Flask development server
    # debug=True enables auto-reloading when you save changes
    # and provides more detailed error messages in the browser.
    # Host '127.0.0.1' means it's only accessible from your own computer.
    # Port 5000 is the default Flask port.
    app.run(host='127.0.0.1', port=5000, debug=True)