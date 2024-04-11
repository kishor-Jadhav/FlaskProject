from app import app
from models.user_model import User_Model
from flask import request
@app.route("/user/getAllUser", methods=['GET'])
def getAllUser():
    model =User_Model()
    return model.getAllUser()

@app.route("/user/getAllUser/<int:uId>", methods=['GET'])
def getUserDetails(uId):
    model =User_Model()
    return model.getUserDetails(uId)

@app.route("/user/addUser/", methods=['POST'])
def addUserDetails():
    model =User_Model()
    return model.addUserDetails(request.form)

@app.route("/user/updateUser/", methods=['POST'])
def updateUserDetails():
    model =User_Model()
    return model.updateUserDetails(request.form)
