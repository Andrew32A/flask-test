#  WHY = we need to be able to collect data from users!
# 1. utilize route variables to get data from the URL
# 2. utilize form data to collect large swaths of information at once!

# importing flask and request (request parses form data)
from flask import Flask, request

# create insteance of flask servers as the root dir within "py file name"
app = Flask(__name__)

# creating some routes
# @ passes a function to another function
@app.route('/')
def displayHomepage():
    return "<h1>Hello world!!</h1>"

@app.route('/route1')
def route1Info():
    return "<h3>Welcome to route 1!</h3>"

# <> denote a route variable
@app.route('/profile/<users_name>')
def profile(users_name):
    return f"<h2>Hello {users_name}!</h2>"

# using multiple route variables
@app.route('/date/<month>/<day>/<year>')
def display_given_date(month, day, year):
    return f"{month} / {day} / {year}"

# creating a <form>!
form_data = f"""
    <form action="/results" method="GET">
        What's your favorite pizza flavor?
        <input type="text" name="pizza_flavor">
        <br>
        What's your favorite crust type?
        <input type="text" name="crust">
        <input type="submit" value="submit pizza!">
    </form>
"""

@app.route('/form_example')
def first_form():
    return form_data

# route that processes our form information
# cool tip: ... = pass
@app.route('/results', methods=['GET'])
def simple_pizza_results():
    pizza_flavor = request.args.get("pizza_flavor")
    crust = request.args.get("crust")
    return f"<h3>A {crust}-crust {pizza_flavor} pizza has been ordered!</h3>"

# turn on server
if __name__ == "__main__":
    app.run(debug=True, port=3000)