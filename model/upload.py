import model.Database as databases
from datetime import datetime
import mysql.connector
import datetime
import pytz

data = databases.Database("localhost","root","","doctor_ai")

def delete_job(id): 
    data.query(f'DELETE FROM results WHERE id = {id}')
    data.commit()
    return data.row_count()

def upload_results(id,query,user_id,user_filename):
    """Upload the results to the database"""
    # tz = pytz.timezone('Europe/Madrid')
    # now = datetime.datetime.now(tz)
    # s = str(now)
    data.query(f"INSERT INTO results (id,query,user_id,user_filename) VALUES ({id},'{query}',{user_id},'{user_filename}')")
    data.commit()
    return True

def update_date(id,result,user_id):
    # tz = pytz.timezone('Europe/Madrid')
    # now = datetime.datetime.now(tz)
    # date = str(now)
    data.query(f"UPDATE results SET result='{result}',date=current_timestamp() WHERE id={id} AND user_id={user_id}")
    data.commit()
    # print("updated")
    return True

def download_results(user_id):
    """Download the results from the database from a specified user"""
    result = data.long_query(f"SELECT * FROM results WHERE user_id={user_id}")
    # print(result)
    return result

def delete_a_results(user_id, id):
    """Delete the results from the database from a specified user"""
    result = data.long_query(f"DELETE FROM results WHERE user_id={user_id} AND id={id}")
    data.commit()
    return result

def select_by_tool(tool,urser_id):
    """Select the results from the database by a specified tool"""
    result = data.long_query(f"SELECT * FROM results WHERE query='{tool}' AND user_id={urser_id}")
    return result
def dddd():
    """Download the results from the database"""
    result = data.query(f"SELECT * FROM results")
    return result

def select_from(field, table):
    """Download the results from the database"""
    result = data.fetch_all(f"SELECT {field} FROM {table}")
    return result

def select_from_where(field,field_two, table,id):
    """Download the results from the database"""
    result = data.query(f"SELECT {field},{field_two} FROM {table} WHERE id={id}")
    return result

def select_from_where_id(field, table,id):
    """Download the results from the database"""
    result = data.query(f"SELECT {field} FROM {table} WHERE id={id}")
    return result

def select_all_where_and(field, table,id):
    result = data.query(f"SELECT * FROM {table} WHERE id={id}")
    # SELECT * FROM `results` WHERE user_id = 1 AND id = 123123;

    return result
