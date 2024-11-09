import pymysql

import datetime



class DatabaseOperations():
    # Fill in the information of the database server.
    __db_url = 'localhost'
    __db_username = 'root' #the name of the username
    __db_password = ''
    __db_name = 'ms'
    __db = ''
    
    def __init__(self):
        """Connect to database when the object is created."""
        self.__db = self.db_connect()
        
    def __del__(self):
        """Disconnect from database when the object is destroyed."""
        self.__db.close()
        
    def db_connect(self):
        self.__db = pymysql.connect(self.__db_url, self.__db_username,
        self.__db_password, self.__db_name)
        return self.__db

    # Web registration
    def register(self, name, gender, education, phone, position):
        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()
        
        # select the last developer
        sql1 = "SELECT Developer_id FROM Developer order by Developer_id desc limit 1"
        sql2 = "SELECT Employee_id FROM employee order by Employee_id desc limit 1"
        
        try:
            # Execute the SQL command
            cursor.execute(sql1)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                developerID = row[0]

            # Increasing developer ID
            developer_str = developerID[0]
            developer_int_str = str(int(developerID[1:]) + 1)
            while len(developer_int_str) < 5:
                developer_int_str = '0' + developer_int_str
            
            #create new developer id
            newdeveloperID = developer_str + developer_int_str
            
            cursor.execute(sql2)
            results2 = cursor.fetchall()
            
            for row in results2:
                developerID = row[0]

             # Increasing employee ID
            developer_str = developerID[0]
            developer_int_str = str(int(developerID[1:]) + 1)
            while len(developer_int_str) < 5:
                developer_int_str = '0' + developer_int_str
            
            #create new employee id
            newemployeeID = developer_str + developer_int_str
            
            #register infomation
            developername = name
            developergender = gender
            developerphone = phone
            developereducation = education
            developerposition = position

            # add a new developer into employee table
            # input the corresponding information
            sql4 = '''Insert into employee(Employee_id, Employee_password, Employee_name, Gender, PhoneNumber, Education)
                  values('%s', 'Zzabc123', '%s', '%s', '%s', '%s')''' % (newemployeeID, developername, developergender, developerphone, developereducation)
            try:
                # Execute the SQL command
                cursor.execute(sql4)
                # Commit your changes in the database.
                db.commit()
            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()

            # add a new developer into developer table
            # input the corresponding information
            sql3 = '''Insert into Developer(Employee_id, Developer_id, Developer_password, Developer_name, Gender, PhoneNumber, Education, Position)
                  values('%s', '%s', 'Zzabc123', '%s', '%s', '%s', '%s', '%s')''' % (newemployeeID, newdeveloperID, developername, developergender, developerphone, developereducation, developerposition)
            try:
                # Execute the SQL command
                cursor.execute(sql3)
                # Commit your changes in the database.
                db.commit()
                return newdeveloperID
            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
            
        except: 
            print("Error: unable to fetch data")


    # show manager's evalation to developer's interface       
    def showRating(self, dID):
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()

        # select manager, developer and grade information of evaluation
        sql = """ select Manager_id, Manager_name, Developer_id, grade
                from (manager natural join evaluate) natural join feedback where developer_id = '%s' """ % (dID)              
        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail" 
        

    # show developer's standing by tasks to developer's interface
    def showStandTask(self, dID):
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()

        # Display task information that should be completed by the developer but whose state is standing by
        sql = """ select project_name, task_id, task_name, task_state, start_time, end_time
                from ((project natural join pro_task) natural join task) natural join finish where task_state = "Standing by" and developer_id = '%s' """ % (dID)              
        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    # show developer's in process tasks to developer's interface
    def showProcessTask(self, dID):
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()

        # Display task information that should be completed by the developer but whose state is in process
        sql = """ select project_name, task_id, task_name, task_state, start_time, end_time
                from ((project natural join pro_task) natural join task) natural join finish where task_state = "In process" and developer_id = '%s' """ % (dID)              
        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    # create a new project and display its information in manager interface
    def createNewProject(self,NewProjectName,mID):
        # Finish this function to query events in given date.

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select last project id (by sql code)
        sql1 = "SELECT Project_id FROM project order by Project_id desc limit 1"
        
        try:

            # Execute the SQL command
            cursor.execute(sql1)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                projectID = row[0]
                
            # increasing the project id    
            project_str = projectID[0]

            project_int_str = str(int(projectID[1:]) + 1)

            # create new project id
            newProjectID = project_str + project_int_str
            
            # insert a new project into project table
            sql2 = '''Insert into project (Project_id, Project_name) values ('%s', '%s')''' % (newProjectID, NewProjectName)

            try:
                # Execute the SQL command
                cursor.execute(sql2)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
                return "fail"

            # insert a new project into creat table
            sql3 = '''Insert into creat (manager_id, project_id) values ('%s', '%s')''' % (mID, newProjectID)

            try:
                # Execute the SQL command
                cursor.execute(sql3)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                db.rollback()
                return "fail"
        
        except:
            # output the waining messages
            print("Error: unable to fetch data")

            # disconnect from server



    # Display information about the project for which the manager is responsible
    def showManagerProject(self, mID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # select project information
        sql = '''select project_id, project_name, manager_name from project natural join creat natural join manager where manager_id = '%s' ''' % (mID)

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # Display task information assigned by manager
    def showAssignTask(self, mID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select task information
        # use the sql code
        sql = ''' with assi_finish(project_id, task_id, manager_id, developer_id) as (select project_id, task_id, manager_id, developer_id from creat natural join pro_task natural join finish where manager_id = '%s')

            select project_name, task_id, task_name, task_state, developer_id from ((project natural join pro_task) natural join task) natural join finish where project_id in (select project_id from assi_finish) and task_state <> "Unevaluated" ''' % (mID)




        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # Display task information not evaluated by manager
    def showUnevalautedTask(self, mID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # select task information
        sql = ''' with assi_finish(project_id, task_id, manager_id, developer_id) as (select project_id, task_id, manager_id, developer_id from creat natural join pro_task natural join finish where manager_id = '%s')

              select project_name, task_id, task_name, task_state, developer_id from ((project natural join pro_task) natural join task) natural join finish where project_id in (select project_id from assi_finish) and task_state = "Unevaluated" ''' % (mID)              


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # manager assign tasks to developer
    def AssignTask(self, pID, taskName, developerID, startDate, endDate):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # get last task id
        sql1 = "SELECT task_id FROM task order by task_id desc limit 1"

        try:

            # Execute the SQL command
            cursor.execute(sql1)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                taskID = row[0]
                
            # increasing task id   
            task_str = taskID[0]

            task_int_str = str(int(taskID[1:]) + 1)
            
            # create new task id
            newTaskID = task_str + task_int_str

            
            # insert a new task to task table
            sql2 = '''Insert into task (task_id, task_name, task_state, start_time, end_time) values ('%s', '%s', '%s', str_to_date('%s','%s'), str_to_date('%s','%s'))''' % (newTaskID, taskName, 'Standing by', startDate, "%Y-%m-%d", endDate, "%Y-%m-%d")
        

        
            try:
                # Execute the SQL command
                cursor.execute(sql2)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                db.rollback()
                return "fail"


            # insert a new task to pro_task table
            sql3 = '''Insert into pro_task (Project_id, task_id) values ('%s', '%s')''' % (pID, newTaskID)

            try:
                # Execute the SQL command
                cursor.execute(sql3)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                db.rollback()
                return "fail"


            # insert a new task to finish table
            sql4 = '''Insert into finish (task_id, developer_id) values ('%s', '%s')''' % (newTaskID, developerID)

            try:
                # Execute the SQL command
                cursor.execute(sql4)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
                return "fail"

        except:
            #output the warning messages
            print("Error: unable to fetch data")

            # disconnect from server



    # manager search project in manager interface
    def SearchProject(self, mID, pID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # select project information
        # use sql code
        sql = ''' with assi_finish(project_id, task_id, manager_id, developer_id) as (select project_id, task_id, manager_id, developer_id from creat natural join pro_task natural join finish where manager_id = '%s')

                  select project_name, task_id, task_name, task_state, developer_id from ((project natural join pro_task) natural join task) natural join finish where project_id in (select project_id from assi_finish) and project_id = '%s'  ''' % (mID, pID)


        

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # manager search task in manager interface
    def SearchTask(self, mID, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # select task information
        sql = ''' with assi_finish(project_id, task_id, manager_id, developer_id) as (select project_id, task_id, manager_id, developer_id from creat natural join pro_task natural join finish where manager_id = '%s')

                  select project_name, task_id, task_name, task_state, developer_id from ((project natural join pro_task) natural join task) natural join finish where project_id in (select project_id from assi_finish) and task_id = '%s' ''' % (mID, tID)


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            # output the result
            return results

        except:

            return "fail"


    # check task state to judge whether it can be deleted
    def getTaskState(self, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # get task state
        sql = ''' select task_state from task where task_id = '%s' ''' % (tID)


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:

                taskState = row[0]

            return taskState

        except:

            return "fail"


    # check task id to judge whether it is assigned by correct manager
    def checkTaskID(self, mID, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # get task id from the database
        sql = '''  with assi_finish(project_id, task_id, manager_id, developer_id) as (select project_id, task_id, manager_id, developer_id from creat natural join pro_task natural join finish where manager_id = '%s')

                   select * from task where task_id = '%s' and task_id in (select task_id from assi_finish) ''' % (mID, tID)

        try:
            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            taskNum = 0

            for row in results:

                taskNum = taskNum + 1

  
            # input task id is wrong
            if(taskNum == 0):

                return False

            # input task id is right
            else:

                return True

        except:
            # output the warning messages
            print("Error: unable to fetch data")

            # disconnect from server

        

        

        

    # manager can delete task
    def deleteTask(self, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # delete task from task table
        sql1 = '''delete from task where task_id = '%s' ''' % (tID)


        try:
            # Execute the SQL command
            cursor.execute(sql1)

            # Commit your changes in the database.
            db.commit()


        except:
            # Rollback in case there is any error
            db.rollback()
            return "fail"
            
        # delete task from pro_task table
        sql2 = '''delete from pro_task where task_id = '%s' ''' % (tID)


        try:
            # Execute the SQL command
            cursor.execute(sql2)

            # Commit your changes in the database.
            db.commit()


        except:
            # Rollback in case there is any error
            # if the input is incorrect then input again
            db.rollback()
            return "fail"
        
        # delete task from finish table
        sql3 = '''delete from finish where task_id = '%s' ''' % (tID)


        try:
            # Execute the SQL command
            cursor.execute(sql3)

            # Commit your changes in the database.
            db.commit()

        except:
            # Rollback in case there is any error
            db.rollback()
            return "fail"


    # developer can start task
    def startTask(self, tID):
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()

        # change task state
        sql = '''UPDATE task SET task_state = 'In process' WHERE task_id = '%s' ''' % (tID)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database.
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
            return "fail"


    # developer can submit task
    def submitTask(self, tID):
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()
        db = DatabaseOperations.db_connect(self)
        cursor = db.cursor()

        # change task state
        sql = '''UPDATE task SET task_state = 'Unevaluated' WHERE task_id = '%s' ''' % (tID)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database.
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
            return "fail"

    # manager can evalaute developer
    def Evaluate(self, mID, dID, tID, grade):


        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        sql1 = "SELECT Feedback_id FROM feedback order by Feedback_id desc limit 1"


        try:

            # Execute the SQL command
            cursor.execute(sql1)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                feedbackID = row[0]
                
            # increasing feedback id    
            feedback_str = feedbackID[0]

            feedback_int_str = str(int(feedbackID[1:]) + 1)

            
            # get new feedback id
            newFeedbackID = feedback_str + feedback_int_str


            # insert new grade into feedback table
            sql2 = '''insert into feedback (Feedback_id, grade) values ('%s', '%s') ''' % (newFeedbackID, grade)


            try:
                # Execute the SQL command
                cursor.execute(sql2)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                db.rollback()
                return "fail"

            # insert new grade into evaluate
            sql3 = '''insert into evaluate (Feedback_id, Manager_id, Developer_id) values ('%s', '%s', '%s') ''' % (newFeedbackID, mID, dID)

            try:
                # Execute the SQL command
                cursor.execute(sql3)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
                return "fail"


            # change task state
            sql4 = '''update task set task_state = 'Completed' where task_id = '%s' ''' % (tID)

            try:
                # Execute the SQL command
                cursor.execute(sql4)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
                return "fail"

        except:
            # output the warning messages
            print("Error: unable to fetch data")
            # disconnect from server


    # change password: to see if user input correct manager id, developer id and password
    def checkEmployee(self, eID, password):


        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # check manager
        # use sql commend
        sql1 = '''select * from manager where Manager_id= '%s' and Manager_password= '%s' ''' % (eID, password)


        try:

            # Execute the SQL command
            cursor.execute(sql1)

            # Fetch all the rows in a list of lists.
            results1 = cursor.fetchall()

            managerNum = 0

            for row in results1:

                managerNum = managerNum + 1


            # check developer
            sql2 = '''select * from developer where Developer_id= '%s' and Developer_password= '%s' ''' % (eID, password)


            try:

                # Execute the SQL command
                cursor.execute(sql2)

                # Fetch all the rows in a list of lists.
                results2 = cursor.fetchall()

                developerNum = 0

                for row in results2:

                    developerNum = developerNum + 1

                # if input wrong id and wrong password
                if(managerNum == 0 and developerNum == 0):

                    return False

                # if input right id and right password
                else:

                    return True

            except:
                # output the warning messages
                print("Error: unable to fetch data")
                # disconnect from server

        except:
            # output the warning messages
            print("Error: unable to fetch data")
            # disconnect from server



    # change manager password
    def changeManagerPassword(self, mID, newPassword):


        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # update new password
        sql1 = ''' update manager set Manager_password = '%s' where Manager_id = '%s' ''' % (newPassword, mID)


        try:
            # Execute the SQL command
            cursor.execute(sql1)

            # Commit your changes in the database.
            db.commit()

          
            employeeID = 'e' + mID[1:]

            
            # update corresponding manager password in employee table
            sql2 = ''' update employee set Employee_password = '%s' where Employee_id = '%s' ''' % (newPassword, employeeID)

            try:
                # Execute the SQL command
                cursor.execute(sql2)

                # Commit your changes in the database.
                db.commit()


            except:
                # Rollback in case there is any error
                # if the input is incorrect then input again
                db.rollback()
                return "fail"

        except:
            # Rollback in case there is any error
            # if the input is incorrect then input again
            db.rollback()
            return "fail"



    # change developer password
    def changeDeveloperPassword(self, dID, newPassword):


        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # update developer password
        sql1 = ''' update developer set Developer_password = '%s' where Developer_id = '%s' ''' % (newPassword, dID)


        try:
            # Execute the SQL command
            cursor.execute(sql1)

            # Commit your changes in the database.
            db.commit()


            sql2 = '''select Employee_id from developer where Developer_id = '%s' ''' % (dID)

            try:

                # Execute the SQL command
                cursor.execute(sql2)

                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()


                for row in results:

                    employeeID = row[0]

                
                # update corresponding developer password in employee table
                sql3 = '''update employee set Employee_password = '%s' where Employee_id = '%s' ''' % (newPassword, employeeID)

                try:
                    # Execute the SQL command
                    cursor.execute(sql3)

                    # Commit your changes in the database.
                    db.commit()

                except:
                    # Rollback in case there is any error
                    # if the input is incorrect then input again
                    db.rollback()
                    return "fail"

            except:
                # output the warning messages
                print("Error: unable to fetch data")
                # disconnect from server

        except:
            # Rollback in case there is any error
            db.rollback()
            return "fail"


    # show all developer information in Developer List web page
    def showDeveloperList(self):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select all developer information
        # use sql command
        sql = '''select Developer_id, Developer_name, Gender, PhoneNumber, Education, Position
               from developer  ''' 


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search developer depend on developerID in Developer List web page
    def SearchDeveloperListID(self, dID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select developer
        sql = '''select Developer_id, Developer_name, Gender, PhoneNumber, Education, Position
                from developer where Developer_id = '%s' '''%(dID)
        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            # output the result
            return results

        except:

            return "fail"

    #search developer depend on developer Name in Developer List web page
    def SearchDeveloperListName(self, dID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select developer
        sql = '''select Developer_id, Developer_name, Gender, PhoneNumber, Education, Position
                from developer where Developer_name = '%s' '''%(dID)
        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    # show all manager information in Manager List web page
    def showManagerList(self):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select manager information
        # use the sql commend
        sql = '''select Manager_id, Manager_name, Gender, PhoneNumber, Education, Department_Name
                from manager natural join  manager_works_in natural join  department
                where manager.Manager_id=manager_works_in.Manager_id and manager_works_in.Department_id = department.Department_ID'''


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    # show all project information in Project List web page
    def showProjectList(self):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select project information
        sql = '''select Project_id, Project_name from project order by Project_id desc  ''' 


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search project depend on projectID in Project List web page
    def SearchProjectID(self, pID):
        
        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select project
        # use the sql command
        sql = '''select Project_id, Project_name from project where Project_id = '%s' '''%(pID)

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search project depend on projectID in Project List web page
    def SearchProjectName(self, pName):
        
        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select project
        sql = '''select Project_id, Project_name from project where Project_name = '%s' '''%(pName)

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    # show all task information in Task List web page
    def showTaskList(self):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        
        # Select the information of the last 10000 tasks
        sql = '''select task_id, task_name,task_state,start_time,end_time
                from task order by task_id desc limit 10000''' 


        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search task depend on taskID in Task List web page
    def SearchTaskID(self, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select task
        sql = '''select task_id, task_name,task_state,start_time,end_time
                 from task where task_id = '%s' '''%(tID)

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search task depend on taskName in Task List web page
    def SearchTaskName(self, tName):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select task
        # use the sql command
        sql = '''select task_id, task_name,task_state,start_time,end_time
                 from task where task_name = '%s' '''%(tName)

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search manager depend on managerID in Manager List web page
    def SearchManagerID(self, mID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select manager
        # use sql command
        sql = '''select Manager_id, Manager_name, Gender, PhoneNumber, Education, Department_Name
                from manager natural join  manager_works_in natural join  department
                where manager.Manager_id=manager_works_in.Manager_id and manager_works_in.Department_id = department.Department_ID
                and Manager_id='%s' '''% (mID)


        

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"

    #search manager depend on managerName in Manager List web page
    def SearchManagerName(self, mName):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select manager
        # use the sql command
        sql = '''select Manager_id, Manager_name, Gender, PhoneNumber, Education, Department_Name
                from manager natural join  manager_works_in natural join  department
                where manager.Manager_id=manager_works_in.Manager_id and manager_works_in.Department_id = department.Department_ID
                and Manager_name='%s' '''% (mName)


        

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # developer can search task in developer interface  
    def SearchDeveloperTaskID(self, dID, tID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select task
        # use the sql command
        sql = """ select project_name, task_id, task_name, task_state, start_time, end_time
                from ((project natural join pro_task) natural join task) natural join finish where developer_id = '%s' and task_id = '%s' """ % (dID, tID) 

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"


    # developer can search project in developer interface
    def SearchDeveloperProjectID(self, dID, pID):

        db = DatabaseOperations.db_connect(self)

        cursor = db.cursor()

        # select project
        # use the sql command 
        sql = """ select project_name, task_id, task_name, task_state, start_time, end_time
                from ((project natural join pro_task) natural join task) natural join finish where developer_id = '%s' and project_id = '%s' """ % (dID, pID) 

        try:

            # Execute the SQL command
            cursor.execute(sql)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            return results

        except:

            return "fail"
        


            

        



                

        

        

        

            
            

        

        

        
        

    

        

        

        
            

        

