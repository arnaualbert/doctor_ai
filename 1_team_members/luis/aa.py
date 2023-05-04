# Imports of the app
from flask              import Flask, render_template, request, session,send_file, redirect, url_for
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from threading          import Thread
from typing             import Union
from random             import *
import model.validators as validate
import model.scripts    as sc
import model.login      as logins
import model.user       as users
import model.iaxray     as ia
import model.upload     as upload
import subprocess
import hashlib
import os
import re
executor = ThreadPoolExecutor(5)
########

########
module_name = __name__
app = Flask(__name__)
####NO TOCAR
###################
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
__path__ = os.getcwd()
path = os.getcwd()
print(path)

def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)

REVERSE= os.path.join(path, 'reverse')
create_directory(REVERSE)



@app.route("/complementary", methods=['GET', 'POST'])
def complementary():
    if not logins.is_logged(): return render_template('login.html') # Validate session

    if request.method == 'GET':
        return render_template('reverse_complementary.html')
    if request.method == 'POST':
        fasta = request.files["reverse_complementary"]
        fasta_ext = fasta.filename
        fasta.save(os.path.join(REVERSE,fasta_ext))
        full_path = os.path.join(REVERSE,fasta_ext)
        if fasta_ext.endswith(".fasta"):
            deamon = Thread(target=sc.complementary_task, args=(full_path,session.get('user_id')),daemon=True)
            deamon.start()
            return render_template('reverse_complementary.html', message="Doing the job")

    return render_template('reverse_complementary.html')