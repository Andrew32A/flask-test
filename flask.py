# importing flask
from flask import Flask

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

# turn on server
if __name__ == "__main__":
    app.run(debug=True, port=3000)