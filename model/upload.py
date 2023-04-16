import model.database as databases
from datetime import datetime
import mysql.connector

data = databases.Database("localhost","admin","1234","doctor_ai")

def upload_results(id,query,result,user_id):
    now = datetime.now()
    s = str(now)
    data.query(f"INSERT INTO results (id,query,result,user_id,date) VALUES ({id},'{query}','{result}',{user_id},'{s}')")
    data.commit()

def download_results(user_id):
    result = data.long_query(f"SELECT * FROM results WHERE user_id={user_id}")
    return result

def dddd():
    result = data.query(f"SELECT * FROM results")
    return result
