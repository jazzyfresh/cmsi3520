from flask import Flask

app = Flask(__name__)

count_num = 0

@app.route("/")
def index():
    return "Thank you for coming to class :)"

@app.route("/hello")
def hello_world():
    return "Hello, world"

@app.route("/count")
def count():
    global count_num 
    count_num += 1
    return f"Count is {count_num}"

@app.route("/json")
def json():
    my_json = {
        "id": "2",
        "name": "Sebastian",
        "type": "human",
        "color": "red",
        "age": 1,
        "valid": True,
        "fri": "oct 11 - only 4 days away!"
    }
    return my_json
