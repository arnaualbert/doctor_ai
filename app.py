from flask import Flask, render_template,request,redirect,url_for
import os

module_name = __name__
app = Flask(__name__)

__path__ = os.getcwd()

@app.route('/', methods=['GET', 'POST'])
def index():
    pass


def create_app():
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='127.0.0.1',port=5000)