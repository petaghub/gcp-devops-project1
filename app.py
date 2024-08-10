from flask import Flask
app = Flask(__name__)
@app.route('/')
def Hello_World():
    return 'Hellow, Simple flask application'