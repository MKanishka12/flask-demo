from flask import Flask ,render_template

app=Flask(__name__)

@app.route('/')
def home():
    print("Flask is running")
    return "hello world"