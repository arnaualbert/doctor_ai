#pip install flask
#from flask import Flask
#app = Flask(__name__)
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # process registration form
#     else:
#         # display registration form

# from flask import render_template

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # process registration form
#     else:
#         return render_template('register.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
        
#         # save user data to database or do other processing
#     else:
#         return render_template('register.html')