from flask import Flask, Blueprint, render_template, request, session
from typing             import Union
import hashlib
import model.login as logins
import model.user as users
import model.upload as upload


import json
from fuzzywuzzy import process


chat_controller = Blueprint('chat_controller', __name__)

def get_value_by_fuzzy_key(json_obj, search_key):
    keys = json_obj.keys()
    closest_match = process.extractOne(search_key, keys)
    print(closest_match)
    if closest_match:
        closest_key = closest_match[0]
        return json_obj[closest_key]
    
    return None


json_tools = '''
{
  "image recognition": "iamlr",
  "local alignment": "localalignment",
  "global alignment": "globalalignment",
  "random sequence": "random_sequence",
  "extract cds": "cdsextract",
  "gb to fasta": "gbtofasta",
  "dna to protein": "dnatoprotein",
  "dna to rna": "dnatorna",
  "split fasta": "split_fasta",
  "complementary": "complementary",
  "reverse complementary": "reverse_complementary"
}
'''


@chat_controller.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == "POST":
        message = request.form["message"]
        parsed_data = json.loads(json_tools)
        url = get_value_by_fuzzy_key(parsed_data, message)
        urls = f'/{url}'
        return Flask.redirect(Flask,location=urls)
        
    # pass