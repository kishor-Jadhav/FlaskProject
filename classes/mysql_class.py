from flask import Flask, jsonify
from flask_mysqldb import MySQL
from app import app

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'backenddb'

mysql = MySQL(app)
class MySQLConnector:
    def __init__(self):
        self.mysql = mysql

    def execute_query(self, query):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query)
        column_names = [desc[0] for desc in cursor.description]         
        rows = cursor.fetchall()
        result = []
        for row in rows:
          row_dict = {}
          for i, col_name in enumerate(column_names):
            row_dict[col_name] = row[i]
          result.append(row_dict)
        print(result)
        cursor.close()
        return result
    
    def execute_insert_query(self, query):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query)     
        self.mysql.connection.commit()   
        cursor.close()
        return "Success"