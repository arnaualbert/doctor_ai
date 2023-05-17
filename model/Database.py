import mysql.connector

class Database:
    """Database class"""
    def __init__(self, host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()


    def query(self, query):
        """Execute a query"""
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def long_query(self, query):
        """Execute a query"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        """Commit changes"""
        self.conn.commit()
    
    def close(self):
        """Close the connection"""
        self.cursor.close()
        self.conn.close()

    def row_count(self):
        return self.cursor.rowcount()

    def fetch_all(self, query):
        """Execute a query"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        # Convertir los resultados a una lista de diccionarios
        columns     = [desc[0] for desc in self.cursor.description]
        result_list = [dict(zip(columns, row)) for row in results]

        return result_list