from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    packages = [
        {"followers": 1000, "price": 10},
        {"followers": 2000, "price": 18},
        {"followers": 3000, "price": 25},
        {"followers": 4000, "price": 30},
        {"followers": 5000, "price": 35},
        {"followers": 6000, "price": 40},
        {"followers": 7000, "price": 45},
        {"followers": 8000, "price": 50},
        {"followers": 9000, "price": 55},
        {"followers": 10000, "price": 60},
    ]
    return render_template('index.html', packages=packages)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
