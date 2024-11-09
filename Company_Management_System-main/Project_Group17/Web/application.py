# Server-side code here.
# If you cannot understand the code below, go to 2.Flask-Templates.

# © 2019-current,
# authors at Computer Science and Technology,
# Division of Science and Technology,
# BNU-HKBU United International College

from flask_wtf import FlaskForm

from wtforms import Form, TextField, IntegerField, SubmitField

from wtforms import Form, StringField, PasswordField, validators

import datetime

from flask import Flask, render_template

from flask import request

from flask_login import LoginManager

from flask_login import UserMixin

from flask_login import login_required

from flask import redirect

from flask_login import login_user

from flask_login import login_required, logout_user

from flask_bootstrap import Bootstrap

import DatabaseOperations

import pymysql

class Admin(UserMixin):
    """User class for flask-login"""
    def __init__(self, id):
        self.id = id
        self.name = 'admin'
        self.password = 'admin'

# login page: get user input username and password
class LoginForm(Form):
    username = StringField('username', [validators.DataRequired()])#Check whether the username is correct
    password = PasswordField('password', [validators.DataRequired()])#Check whether the password is correct

# check login
class DatabaseOperations1():
    # Fill in the information of your database server.
    __db_url = 'localhost'
    __db_username = 'root'
    __db_password = ''
    __db_name = 'ms'
    __db = ''
    def _init_(self):
        """Connect to database when the object is created."""
        self.__db = self.db_connect()
    def __del__(self):
        """Disconnect from database when the object is destroyed."""
        self.__db.close()
    def db_connect(self):
        self.__db = pymysql.connect(self.__db_url, self.__db_username,
        self.__db_password, self.__db_name)
        return self.__db
    def select(self,sql):
        db = DatabaseOperations1.db_connect(self)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            raise e
        finally:
            cursor.close()

app = Flask(__name__)
bootstrap=Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = b'my-secret-key'
mID = "Admin"
dID = "User"

@login_manager.user_loader
def load_user(user_id):
    return Admin(user_id)

# index page
@app.route('/')
def index():
    return render_template('index.html')

# login web page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        pwd = form.password.data
        sql = DatabaseOperations1()
        check = list(username)
        global mID
        global dID

        if(username == "" or pwd == ""):#if do not input

            message = "Input can not be null!"

            return render_template('login.html', message = message)

        # check manager id and manager password
        if(check[0] == 'm'):
            tup = sql.select("select * from manager where Manager_id='"+username+"'and Manager_password='"+pwd+"';")
            num = 0
            mID = username
            for data in tup:
                num = num + 1
            if (num != 0):#if input right, go to manager page
                test_admin_user = Admin(username)
                login_user(test_admin_user)
                return redirect('./Manager')
            else:
                message = "Login fail! ID or password wrong!"#if input wrong,warning
                return render_template('login.html', message = message)

        # check developer id and developer password,similar as manager
        elif(check[0] == 'd'):
            tup = sql.select("select * from developer where Developer_id='"+username+"'and Developer_password='"+pwd+"';")
            num = 0
            dID = username
            for data in tup:
                num = num + 1
            if (num != 0):
                test_admin_user = Admin(username)
                login_user(test_admin_user)
                return redirect('./Developer')#if input right, go to developer page
            else:
                message = "Login fail! ID or password wrong!"
                return render_template('login.html', message = message)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

# register web page
@app.route('/Update', methods=['GET', 'POST'])
def Update():
    if request.method == 'POST':
        if (request.form['button'] == 'Submit'):

            # get new developer's information
            name = request.form['NewDeveloperName']
            gender = request.form['gender']
            education = request.form['education']
            phone = request.form['NewDeveloperPhoneNumber']
            position = request.form['NewDeveloperPosition']

            # if the input is null, return a warning
            if(name == "" or phone == "" or position == ""):
                alter = "Input can not be null!"

                return render_template('Update.html', alter = alter)

            # add a new developer
            else:
                newEmployeeObject = DatabaseOperations.DatabaseOperations()
                newEmployee = newEmployeeObject.register(name,gender,education,phone,position)
                alter = "Successfull, welcome " + name + " , your ID is " + newEmployee
                return render_template('Update.html', alter = alter)
    else:
        alter = ''
        return render_template('Update.html', alter = alter)


# change password web page
@app.route('/ChangePW', methods=['GET', 'POST'])
def ChangePW():

    if request.method == 'POST':

        if (request.form['button'] == 'SaveUpdate'):
            
            # get input information
            eID = request.form['EmployeeID']

            password = request.form['EmployeePassword']

            newPassword = request.form['UpdateEmployeePassword']

            checkPassword = request.form['CheckEmployeeNewPassword']

            
            # if the input is null, return a warning
            if(eID == "" or password == "" or newPassword == "" or checkPassword == ""):

                message = "Input can not be null"
                return render_template('ChangePW.html', message = message)


            # check whether the employee input correct manager id or developer id and password
            else:
            

                checkEmployeeObject = DatabaseOperations.DatabaseOperations()

                checkEmployee = checkEmployeeObject.checkEmployee(eID, password)

                # if the input id and password are not correct, return a warning
                if(checkEmployee == False):

                    message = "Employee id or password wrong!"

                    return render_template('ChangePW.html', message = message)

                # if the passwords entered before and after are inconsistent, return a warning
                elif (newPassword != checkPassword):

                    message = "The passwords entered before and after are inconsistent!"

                    return render_template('ChangePW.html', message = message)

                # change manager password
                else:

                    if(eID[0] == 'm'):

                        changeManagerPasswordObject = DatabaseOperations.DatabaseOperations()

                        changeManagerPasswordObject.changeManagerPassword(eID, newPassword)

                        message = "New password save successfully!"

                        return render_template('ChangePW.html', message = message)

                    # change developer password
                    if(eID[0] == 'd'):

                        changeDeveloperPasswordObject = DatabaseOperations.DatabaseOperations()

                        changeDeveloperPasswordObject.changeDeveloperPassword(eID, newPassword)

                        message = "New password save successfully!"

                        return render_template('ChangePW.html', message = message)

                    

    else:

        return render_template('ChangePW.html')


# manager interface
@app.route('/Manager', methods=['GET', 'POST'])
@login_required
def Manager():
    global mID

    # show project information
    projectListObject = DatabaseOperations.DatabaseOperations()

    projectList = projectListObject.showManagerProject(mID)


    # show assigned task information
    taskListObject = DatabaseOperations.DatabaseOperations()

    taskList = taskListObject.showAssignTask(mID)


    # show unevaluated task information
    unevaluatedListObject = DatabaseOperations.DatabaseOperations()

    UnevaluatedTaskList = unevaluatedListObject.showUnevalautedTask(mID)


    # create new project
    if request.method == 'POST':
         if (request.form['button'] == 'Create Project'):
            NewProjectName = request.form['NewProjectName']
            if NewProjectName == "":
                error = "Input cannot be null!"
                return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, error = error)

            else:
                
                NewProjectObject = DatabaseOperations.DatabaseOperations()
                NewProjectObject.createNewProject(NewProjectName,mID)
                return redirect('Manager')

    # assign task
    if request.method == 'POST':

        if (request.form['button'] == 'Assign Task'):

            assignProjectID = request.form['ProjectID']

            assignTaskName = request.form['TaskName']

            assignDeveloperID = request.form['DeveloperID']

            assignStartDate = request.form['StartDate']

            assignEndDate = request.form['EndDate']

            if (assignProjectID == "" or assignTaskName == "" or assignDeveloperID == "" or assignStartDate == "" or assignEndDate == ""):

                message = "Input cannot be null!"

                return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)

            else:


                NewTaskObject = DatabaseOperations.DatabaseOperations()
            
                NewTaskObject.AssignTask(assignProjectID, assignTaskName, assignDeveloperID, assignStartDate, assignEndDate)

                return redirect('Manager')

    # search project
    if request.method == 'POST':

         if (request.form['button'] == 'Search'):

             if(request.form['SearchType'] == 'SearchProjectName'):

                 pID = request.form['SearchID']

                 if(pID == ""):

                     message = "Input cannot be null!"

                     return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)

                 else:
                     taskListObject = DatabaseOperations.DatabaseOperations()

                     taskList = taskListObject.SearchProject(mID, pID)

                     return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList)

    # search task 
    if request.method == 'POST':

         if (request.form['button'] == 'Search'):

             if(request.form['SearchType'] == 'SearchTaskName'):

                 tID = request.form['SearchID']

                 if(tID == ""):

                     message = "Input cannot be null!"

                     return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)

                 else:

                     taskListObject = DatabaseOperations.DatabaseOperations()

                     taskList = taskListObject.SearchTask(mID, tID)

                     return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList)

    # delete task error: can not delete tasks that are assigned by other manager
    if request.method == 'POST':

         if (request.form['button'] == 'Delete Task'):

             tID = request.form['DeleteTask']

             if(tID == ""):
                 
                 message = "Input cannot be null!"
                 return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)

             else:

                 checkTaskObject = DatabaseOperations.DatabaseOperations()

                 checkTask = checkTaskObject.checkTaskID(mID, tID)

                 if(checkTask == False):

                     message = "Prohibit deleting tasks that are not assigned by you!"
                     return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)

    # delete task
    if request.method == 'POST':

        if (request.form['button'] == 'Delete Task'):

             tID = request.form['DeleteTask']

             if(tID == ""):

                 message = "Input cannot be null!"
                 return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)


             taskStateObject = DatabaseOperations.DatabaseOperations()

             taskState = taskStateObject.getTaskState(tID)

             # can not delete a task whose state is in process or unevalaued
             if(taskState == "In process" or taskState == "Unevaluated"):

                 message = "Cannot delete a task in progress or Unevaluated!"

                 return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, message = message)


             else:

                 taskStateObject = DatabaseOperations.DatabaseOperations()

                 taskState = taskStateObject.getTaskState(tID)

                 if(taskState != "In process" and taskState != "Unevaluated"):

                     taskDeleteObject = DatabaseOperations.DatabaseOperations()

                     taskDeleteObject.deleteTask(tID)

                     return redirect('Manager')

    # evaluate developer
    if request.method == 'POST':

         if (request.form['button'] == 'Evaluate'):

             dID = request.form['EvaluatedDeveloperID']

             tID = request.form['EvaluatedTaskID']

             grade = request.form['grade']

             if(dID == "" or tID == ""):

                 error2 = "Input cannot be null!"

                 return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList, error2 = error2)

             else:

                 EvaluateObject = DatabaseOperations.DatabaseOperations()
                 EvaluateObject.Evaluate(mID, dID, tID, grade)
                 return redirect('Manager')


    else:
        return render_template('Manager.html', projectList = projectList, taskList = taskList, UnevaluatedTaskList = UnevaluatedTaskList)


# developer interface
@app.route('/Developer', methods=['GET', 'POST'])
@login_required
def Developer():
    global dID

    # show in process task
    startlistObject = DatabaseOperations.DatabaseOperations()
    startList = startlistObject.showProcessTask(dID)

    # show standing by task
    standinglistObject = DatabaseOperations.DatabaseOperations()
    standingList = standinglistObject.showStandTask(dID)

    # show evalaution 
    RatingObject = DatabaseOperations.DatabaseOperations()
    Rating = RatingObject.showRating(dID)

    # start task
    if (request.method == 'POST'):
            if (request.form['button'] == 'start'):
                tID = request.form['StartTask']
                taskStateObject = DatabaseOperations.DatabaseOperations()
                taskState = taskStateObject.getTaskState(tID)
                if(taskState == "Standing by"):
                    taskDeleteObject = DatabaseOperations.DatabaseOperations()
                    taskDeleteObject.startTask(tID)
                    return redirect('Developer')
                else:
                    message = "Wrong input"
                    return render_template('Developer.html', standinglist = standingList, startlist = startList, message = message, Rating = Rating)

    # submit task
    if (request.method == 'POST'):
            if (request.form['button'] == 'submit'):
                tID = request.form['SubmitTask']
                taskStateObject = DatabaseOperations.DatabaseOperations()
                taskState = taskStateObject.getTaskState(tID)
                if(taskState == "In process"):
                    taskDeleteObject = DatabaseOperations.DatabaseOperations()
                    taskDeleteObject.submitTask(tID)
                    return redirect('Developer')
                else:
                    message = "Wrong input"
                    return render_template('Developer.html', standinglist = standingList, startlist = startList, message = message, Rating = Rating)

    # search task and project
    if (request.method == 'POST'):

         if (request.form['button'] == 'Search'):

            if(request.form['type'] == 'tID'):
                tID = request.form['info']

                taskListObject = DatabaseOperations.DatabaseOperations()

                standingList = taskListObject.SearchDeveloperTaskID(dID, tID)

                return render_template('Developer.html', standinglist = standingList, startlist = startList, Rating = Rating)
                
            else:
                pID = request.form['info']

                taskListObject = DatabaseOperations.DatabaseOperations()

                standingList = taskListObject.SearchDeveloperTaskID(dID, pID)

                return render_template('Developer.html', standinglist = standingList, startlist = startList, Rating = Rating)
    else:
        return render_template('Developer.html', standinglist = standingList, startlist = startList, Rating = Rating)

# developer list interface
@app.route('/DeveloperList', methods=['GET', 'POST'])
@login_required
def DeveloperList():
    global mID
    global dID

    # show developer information
    developerListObject = DatabaseOperations.DatabaseOperations()

    developerList = developerListObject.showDeveloperList()
    if request.method == 'POST':

        if(request.form['button'] == 'Home'):
            if(dID == "User" and mID != "Admin"):
                return redirect('Manager')
            if(dID != "User" and mID == "Admin"):
                return redirect('Developer')

    # search developer depend on developer id
    if request.method == 'POST':

        if(request.form['button'] == 'Search Developer'):

            if(request.form['SearchType'] == 'SearchDeveloperID'):

                dID =  request.form['SearchID']

                if(dID == ""):
                    error = "Input can not be null"
                    return render_template('DeveloperList.html', developerList=developerList, error = error)

                else:   

                    developerListObject = DatabaseOperations.DatabaseOperations()

                    developerList = developerListObject.SearchDeveloperListID(dID)

                    return render_template('DeveloperList.html', developerList=developerList)

            # search developer depend on developer name
            if(request.form['SearchType'] == 'SearchDeveloperName'):

                dName =  request.form['SearchID']

                if(dName == ""):
                    error = "Input can not be null"
                    return render_template('DeveloperList.html', developerList=developerList, error = error)

                else:

                    developerListObject = DatabaseOperations.DatabaseOperations()

                    developerList = developerListObject.SearchDeveloperListName(dName)

                    return render_template('DeveloperList.html', developerList=developerList)

    else:
        developerListObject = DatabaseOperations.DatabaseOperations()

        developerList = developerListObject.showDeveloperList()

        return render_template('DeveloperList.html', developerList=developerList)


# manager list web page
@app.route('/ManagerList', methods=['GET', 'POST'])
@login_required
def ManagerList():

    # show manager information
    managerListObject = DatabaseOperations.DatabaseOperations()

    managerList = managerListObject.showManagerList()
    global mID
    global dID
    if request.method == 'POST':

        if(request.form['button'] == 'Home'):

            if(dID == "User" and mID != "Admin"):
                return redirect('Manager')

            if(dID != "User" and mID == "Admin"):

                return redirect('Developer')

    # search manager depend on manager id
    if request.method == 'POST':

        if (request.form['button'] == 'Search'):

            if(request.form['SearchType'] == 'ManagerID'):

                mID = request.form['SearchID']

                if(mID == ""):
                    error = "Input can not be null!"

                    return render_template('ManagerList.html',managerList=managerList, error = error)

                else:
                    managerListObject = DatabaseOperations.DatabaseOperations()
                    managerSearchList = managerListObject.SearchManagerID(mID)
                    return render_template('ManagerList.html', managerList=managerSearchList)

            # search manager depend on manager name
            if(request.form['SearchType'] == 'ManagerName'):

                mName = request.form['SearchID']

                if(mName == ""):

                    error = "Input can not be null!"
                    return render_template('ManagerList.html',managerList=managerList, error = error)

                else:
                    managerListObject = DatabaseOperations.DatabaseOperations()
                    managerSearchList = managerListObject.SearchManagerName(mName)
                    return render_template('ManagerList.html', managerList=managerSearchList)

    else:
        return render_template('ManagerList.html',managerList=managerList)

# project list web page
@app.route('/Project_List', methods=['GET', 'POST'])
@login_required
def Project_List():

    # show project information
    ProjectListAllObject = DatabaseOperations.DatabaseOperations()

    projectListAll = ProjectListAllObject.showProjectList()
    global mID
    global dID
    if request.method == 'POST':
        if(request.form['button'] == 'Home'):
            if(dID == "User" and mID != "Admin"):
                return redirect('Manager')
            if(dID != "User" and mID == "Admin"):
                return redirect('Developer')

    # search project depend on project id
    if request.method == 'POST':

        if (request.form['button'] == 'Search'):

            if(request.form['SearchType'] == 'ProjectID'):

                pID = request.form['SearchID']

                if(pID == ""):

                    error = "Input can not be null!"

                    return render_template('Project_List.html',projectListAll=projectListAll, error = error)

                else:

                    ProjectListAllObject = DatabaseOperations.DatabaseOperations()

                    projectListAll = ProjectListAllObject.SearchProjectID(pID)

                    return render_template('Project_List.html', projectListAll=projectListAll)

            # search project depend on project name
            if(request.form['SearchType'] == 'ProjectName'):

                pName = request.form['SearchID']

                if(pName == ""):

                    error = "Input can not be null!"

                    return render_template('Project_List.html',projectListAll=projectListAll, error = error)

                else:

                    ProjectListAllObject = DatabaseOperations.DatabaseOperations()

                    projectListAll = ProjectListAllObject.SearchProjectName(pName)

                    return render_template('Project_List.html', projectListAll=projectListAll)
            
    else:

        return render_template('Project_List.html',projectListAll=projectListAll)

# suggestion web page
@app.route('/suggestion', methods=['GET', 'POST'])
@login_required
def suggestion():
    return render_template('suggestion.html')


# Task List web page
@app.route('/Task_List', methods=['GET', 'POST'])
@login_required
def Task_List():

    # show task information
    TaskListAllObject = DatabaseOperations.DatabaseOperations()

    taskListAll = TaskListAllObject.showTaskList()

    global mID
    global dID
    if request.method == 'POST':

        if(request.form['button'] == 'Home'):

            if(dID == "User" and mID != "Admin"):

                return redirect('Manager')

            if(dID != "User" and mID == "Admin"):

                return redirect('Developer')

    # search task depend on task id 
    if request.method == 'POST':

        if (request.form['button'] == 'Search'):

            if(request.form['SearchType'] == 'TaskID'):

                tID = request.form['SearchID']

                if(tID == ""):

                    error = "Input can not be null!"

                    return render_template('Task_List.html',taskListAll=taskListAll, error = error)

                else:

                    TaskListAllObject = DatabaseOperations.DatabaseOperations()

                    taskListAll = TaskListAllObject.SearchTaskID(tID)

                    return render_template('Task_List.html', taskListAll=taskListAll)


            # search task depend on task name
            if(request.form['SearchType'] == 'TaskName'):

                tName = request.form['SearchID']

                if(tName == ""):

                    error = "Input can not be null!"

                    return render_template('Task_List.html',taskListAll=taskListAll, error = error)

                else:

                    TaskListAllObject = DatabaseOperations.DatabaseOperations()

                    taskListAll = TaskListAllObject.SearchTaskName(tName)

                    return render_template('Task_List.html', taskListAll=taskListAll)

    else:

        return render_template('Task_List.html',taskListAll=taskListAll)

# Manual web page    
@app.route('/Manual', methods=['GET', 'POST'])
def Manual():
    return render_template('Manual.html')

# log out
@app.route('/logout')
@login_required
def logout():
    global mID
    global dID
    mID = "Admin"
    dID = "User"
    logout_user()
    # Redirect to homepage
    return redirect('login')
