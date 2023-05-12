from flask import Flask, Blueprint, render_template, request, session
from typing             import Union
import hashlib
import model.login as logins
import model.user as users
import model.upload as upload

chat_controller = Blueprint('chat_controller', __name__)



@chat_controller.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == "POST":
        message = request.form["message"]
        url = f'/{message}'
        return Flask.redirect(Flask,location=url)
        
    # pass