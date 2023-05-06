from flask import Blueprint, render_template, request, session
from typing             import Union
import hashlib
import model.login as logins
import model.user as users
import model.upload as upload

database_controller = Blueprint('database_controller', __name__)


@database_controller.route('/history', methods=['GET', 'POST'])
def history():
    """Show the history page"""
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        # Show the history
        user_id = session.get('user_id')
        list_of_results = upload.download_results(user_id)
        results = list_of_results
        return render_template('history.html',results=results)

    return render_template('history.html')

@database_controller.route('/history_query', methods=['GET', 'POST'])
def history_query():
    """Show the history page"""
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'POST':
        # Show the history
        user_id = session.get('user_id')
        tool = request.form['query_order']
        list_of_results = upload.select_by_tool(tool,user_id)
        results = list_of_results
        return render_template('history.html',results=results)
    return render_template('history.html')