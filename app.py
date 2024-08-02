from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "gaurav"  # Consider using a more secure secret key

@app.route("/hello")
def index():
    """Renders the index template with a flash message asking for the user's name"""
    flash("What's your name?")
    return render_template("/index.html")

@app.route("/greet", methods=["POST"])  # Only allow POST requests
def greet():
    """Handles the form submission, flashes a greeting message, and renders the index template"""
    name = request.form.get("name_input")  # Use the get method to avoid KeyError
    if name:
        flash(f"Hi {name}! It's great to see you!")  # Use an f-string for a more readable message
    else:
        flash("Please enter your name.")  # Handle the case where the name is not provided
    return render_template("/index.html")