from flask import Flask, render_template



# Create Flask Instance
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)  # Auto-reloads on code changes

# Create a route
@app.route("/")
def index() :
    return "<hl>Hello World !!! <h1/>"


@app.route("/help")
def help(): 
    return "<h1>Help<h1/>"

@app.route("/user/<name>")
def user(name) :
    return "<hl>Hello World {}!!!<h1/>".format(name)