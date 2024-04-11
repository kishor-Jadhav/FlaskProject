from classes.mysql_class import  MySQLConnector
from flask import Flask, jsonify
import json
class User_Model:
    def __init__(self):
        self.db = MySQLConnector()
         

    def getAllUser(self):                 
         sql= "select * from user_info"
         result = self.db.execute_query(sql)
         if result:             
             return jsonify(result) 
         else:
             return "No Data"

    def getUserDetails(self,uId):                 
         sql= f"select * from user_info where userId='{uId}'"
         print(sql)
         result = self.db.execute_query(sql)
         if result:             
             return jsonify(result) 
         else:
             return "No Data"    
         
    def addUserDetails(self,data):                 
         sql= f"insert into user_info (userName,age,emailId,pass) values ('{data['userName']}','{data['age']}','{data['emailId']}','{data['pass']}')"
         print(sql)
         result = self.db.execute_insert_query(sql)
         if result=='Success':             
             return 'Success' 
         else:
             return "No Data"  

    def updateUserDetails(self,data):                 
         sql= f"update user_info set userName='{data['userName']}',age='{data['age']}',emailId='{data['emailId']}',pass='{data['emailId']}'  where userId='{data['userId']}'"
         print(sql)
         result = self.db.execute_insert_query(sql)
         if result=='Success':             
             return 'Update Success' 
         else:
             return "No Data"             
             
         
         