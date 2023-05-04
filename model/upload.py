import model.database as databases
from datetime import datetime
import mysql.connector
import datetime
import pytz

data = databases.Database("localhost","root","","doctor_ai")

def delete_job(id): 
    data.query(f'DELETE FROM results WHERE id = {id}')
    data.commit()
    return data.row_count()
def upload_results(id,query,result,user_id):
    """Upload the results to the database"""
    tz = pytz.timezone('Europe/Madrid')
    now = datetime.datetime.now(tz)
    s = str(now)
    data.query(f"INSERT INTO results (id,query,result,user_id,date) VALUES ({id},'{query}','{result}',{user_id},'{s}')")
    data.commit()
    return True

def download_results(user_id):
    """Download the results from the database from a specified user"""
    result = data.long_query(f"SELECT * FROM results WHERE user_id={user_id}")
    return result

def delete_a_results(user_id, id):
    """Download the results from the database from a specified user"""
    result = data.long_query(f"DELETE * FROM results WHERE user_id={user_id} AND id='{id}'")
    return result

def select_by_tool(tool,urser_id):
    """Select the results from the database by a specified tool"""
    result = data.long_query(f"SELECT * FROM results WHERE query='{tool}' AND user_id={urser_id}")
    return result
def dddd():
    """Download the results from the database"""
    result = data.query(f"SELECT * FROM results")
    return result
