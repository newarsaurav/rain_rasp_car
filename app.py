from flask import Flask, render_template
from engine import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<direction>')
def move(direction):
    actions = {
        "forward": forward,
        "backward": backward,
        "left": left,
        "right": right,
        "stop": stop
    }

    if direction in actions:
        actions[direction]()
        print(f"the derection is {direction} ")
        return f"Car moving {direction}"
    else:
        return "Invalid direction", 400



# if __name__ == '__main__':
    # app.run(debug=True , host= "0.0.0.0")
    
