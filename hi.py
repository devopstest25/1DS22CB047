from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Hii")
    return "New Branch"

app.run()