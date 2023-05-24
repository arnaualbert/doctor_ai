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
    """Get the value of a key in a json object"""
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
  "recognize":"iamlr",
  "image":"iamlr",
  "to recognize":"iamlr",
  "detect":"iamlr",
  "to detect":"iamlr",
  "local":"localalignment",
  "lung":"iamlr",
  "brain":"iamlr",
  "to align":"localalignment",
  "local alignment": "localalignment",
  "global alignment": "globalalignment",
  "random sequence": "random_sequence",
  "extract cds": "cdsextract",
  "gb to fasta": "gbtofasta",
  "genbank to fasta": "gbtofasta",
  "genbank":"gbtofasta",
  "dna to protein": "dnatoprotein",
  "translate this dna":"dnatoprotein",
  "dna to rna": "dnatorna",
  "to split a fasta":"split_fasta",
  "split fasta": "split_fasta",
  "to do a complementary":"complementary",
  "complementary": "complementary",
  "to do a reverse":"reverse_complementary",
  "reverse complementary": "reverse_complementary",
  "logout":"logout",
  "log out": "logout"
}
'''


@chat_controller.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == "POST":
        # Get the data from the form
        message = request.form["message"]
        parsed_data = json.loads(json_tools)
        url = get_value_by_fuzzy_key(parsed_data, message)
        urls = f'/{url}'
        # redirect
        return Flask.redirect(Flask,location=urls)
        
    # pass