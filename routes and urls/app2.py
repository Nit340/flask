from flask import Flask  

app = Flask(__name__)  

# Home route
@app.route('/')  
def home():  
    return "Welcome to Flask!"  

# About route
@app.route('/about')  
def about():  
    return "This is the About page."  

# Dynamic route with a variable (name)
@app.route('/user/<name>')  
def user(name):  
    return f"Hello, {name}!"  

if __name__ == '__main__':  
    app.run(debug=True)  
