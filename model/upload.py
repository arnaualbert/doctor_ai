import model.database as databases
from datetime import datetime
import mysql.connector

data = databases.Database("localhost","root","","doctor_ai")

def upload_results(id,query,result,user_id):
    """Upload the results to the database"""
    now = datetime.now()
    s = str(now)
    data.query(f"INSERT INTO results (id,query,result,user_id,date) VALUES ({id},'{query}','{result}',{user_id},'{s}')")
    data.commit()

def download_results(user_id):
    """Download the results from the database from a specified user"""
    result = data.long_query(f"SELECT * FROM results WHERE user_id={user_id}")
    return result

def dddd():
    """Download the results from the database"""
    result = data.query(f"SELECT * FROM results")
    return result
