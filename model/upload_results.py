import model.database as databases
import mysql.connector

data = databases.Database("localhost","root","","doctor_ai")

def upload_results(id,query,result,user_id):
    data.query(F"INSERT INTO result (id,query,result,user_id) VALUES ({id},'{query}','{result}',{user_id})")
    data.commit()
    