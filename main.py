from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<direction>')
def move(direction):
    
    print(f"Moving {direction}")
    return f"Car moving {direction}"

if __name__ == '__main__':
    app.run(debug=True)
