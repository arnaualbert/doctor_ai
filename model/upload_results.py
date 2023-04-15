import model.database as databases
import mysql.connector

data = databases.Database("localhost","root","","doctor_ai")

def upload_results(id,query,result,user_id):
    data.query(f"INSERT INTO results (id,query,result,user_id) VALUES ({id},'{query}','{result}',{user_id})")
    data.commit()

def download_results(user_id):
    data.query(f"SELECT * FROM results WHERE user_id='{user_id}'")
    