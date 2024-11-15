// server.js (修改后的代码)
const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const path = require('path');

// 设置静态文件目录（假设文件在项目的根目录下）
app.use(express.static(path.join(__dirname)));
app.use(cors());
app.use(bodyParser.json());

// 创建 MySQL 连接到 'employee_management' 数据库（用于用户管理）
const employeeDB = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'employee_management'
});

// 创建 MySQL 连接到 'project_task_db' 数据库（用于项目和任务管理）
const projectTaskDB = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'project_task_db'
});

// 创建 MySQL 连接到 'new_project_task_db' 数据库（用于项目和任务管理）
const newprojectTaskDB = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'new_project_task_db'
});

// 创建 MySQL 连接到 'department_management_db' 数据库（用于项目和任务管理）
const DepartmentManagementDB = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'department_management'
});

// 创建 MySQL 连接到 'ProjectManagementSystem' 数据库（用于项目和任务管理）
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'ProjectManagementSystem'
});

// 连接到 'employee_management' 数据库
employeeDB.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to employee_management database...');
});

// 连接到 'project_task_db' 数据库
projectTaskDB.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to project_task_db database...');
});

// 连接到 'new_project_task_db' 数据库
newprojectTaskDB.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to new_project_task_db database...');
});

// 连接到 'department_management' 数据库
DepartmentManagementDB.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to department_management database...');
});

// 连接到 'department_management' 数据库
db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to ProjectManagementSystem database...');
});

// -------------------- 登录功能（使用 employee_management 数据库） -------------------- //
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    const queryDeveloper = "SELECT * FROM developer WHERE Developer_id = ? AND Developer_password = ?";
    employeeDB.query(queryDeveloper, [username, password], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            res.json({ success: true, role: 'developer', username: username });
        } else {
            const queryManager = "SELECT * FROM manager WHERE Manager_id = ? AND Manager_password = ?";
            employeeDB.query(queryManager, [username, password], (err, results) => {
                if (err) throw err;
                if (results.length > 0) {
                    res.json({ success: true, role: 'manager', username: username, managerID: results[0].Manager_id });
                } else {
                    res.json({ success: false, message: 'Invalid credentials' });
                }
            });
        }
    });
});

// -------------------- 获取用户详细信息（根据角色选择） -------------------- //
app.get('/user-info', (req, res) => {
    const role = req.query.role;
    const username = req.query.username;

    if (role === 'developer') {
        const query = "SELECT Employee_id, Developer_id, Developer_name as name, Gender, PhoneNumber, Education, Position FROM developer WHERE Developer_id = ?";
        employeeDB.query(query, [username], (err, result) => {
            if (err) throw err;
            if (result.length > 0) {
                res.json(result[0]);
            } else {
                res.status(404).json({ message: 'Developer not found' });
            }
        });
    } else if (role === 'manager') {
        const query = "SELECT Manager_id, Employee_id, Manager_name as name, Gender, PhoneNumber, Education FROM manager WHERE Manager_id = ?";
        employeeDB.query(query, [username], (err, result) => {
            if (err) throw err;
            if (result.length > 0) {
                res.json(result[0]);
            } else {
                res.status(404).json({ message: 'Manager not found' });
            }
        });
    } else {
        res.status(400).json({ message: 'Invalid role' });
    }
});

// -------------------- 项目检查（使用 project_task_db 数据库） -------------------- //
app.post('/check-project', (req, res) => {
    const { projectID, projectName } = req.body;

    const checkProjectQuery = "SELECT * FROM project WHERE project_id = ? OR project_name = ?";
    projectTaskDB.query(checkProjectQuery, [projectID, projectName], (err, results) => {
        if (err) throw err;

        if (results.length > 0) {
            res.json({ success: false, message: 'Project ID or Project Name already exists' });
        } else {
            res.json({ success: true, message: 'Project ID and Name are available' });
        }
    });
});

// -------------------- 任务检查（使用 project_task_db 数据库） -------------------- //
app.post('/check-task', (req, res) => {
    const { taskID, taskName } = req.body;

    const checkTaskQuery = "SELECT * FROM task WHERE task_id = ? OR task_name = ?";
    projectTaskDB.query(checkTaskQuery, [taskID, taskName], (err, results) => {
        if (err) throw err;

        if (results.length > 0) {
            res.json({ success: false, message: 'Task ID or Task Name already exists' });
        } else {
            res.json({ success: true, message: 'Task ID and Name are available' });
        }
    });
});

// -------------------- 验证 Manager ID 的功能（保持不变，使用 employee_management 数据库） -------------------- //
app.post('/verify-manager', (req, res) => {
    const { managerID, loggedInManagerID } = req.body;

    if (managerID === loggedInManagerID) {
        res.json({ success: true });
    } else {
        res.json({ success: false, message: '无效的 Manager ID' });
    }
});

// -------------------- 获取未评估任务的 Task ID 列表 -------------------- //
app.get('/api/unevaluated-tasks', (req, res) => {
    const query = "SELECT task_id FROM task WHERE task_state = 'Unevaluated'";
    projectTaskDB.query(query, (err, results) => {
        if (err) {
            console.error('Error fetching tasks:', err);
            res.status(500).send('Server error');
            return;
        }
        res.json(results);
    });
});

// -------------------- 根据 Task ID 获取 Developer ID -------------------- //
app.get('/api/task-developer', (req, res) => {
    const { taskID } = req.query;

    if (!taskID) {
        return res.status(400).json({ message: 'Task ID is required' });
    }

    // 修改后的 SQL 查询：从 task 表获取 task_state，并通过 task_id 关联 finish 表
    const query = `
        SELECT f.developer_id
        FROM task t
        JOIN finish f ON t.task_id = f.task_id
        WHERE t.task_id = ? AND t.task_state = 'Unevaluated'`;

    projectTaskDB.query(query, [taskID], (err, results) => {
        if (err) {
            console.error('Error fetching developer:', err);
            return res.status(500).send('Server error');
        }

        if (results.length === 0) {
            return res.status(404).json({ message: 'No developer found for this task' });
        }

        res.json(results[0]);
    });
});

// -------------------- 获取所有任务信息（使用 new_project_task_db 数据库） -------------------- //
app.get('/api/all-tasks', (req, res) => {
    const { task_state } = req.query;
    let query = "SELECT task_id, task_name, task_state, start_time, end_time FROM task";
    
    // If a task_state is provided, add a WHERE clause
    if (task_state) {
        query += " WHERE task_state = ?";
    }

    newprojectTaskDB.query(query, task_state ? [task_state] : [], (err, results) => {
        if (err) {
            console.error('Error fetching tasks:', err);
            res.status(500).send('Server error');
            return;
        }
        res.json(results);
    });
});


// -------------------- 获取部门信息：开发者和经理 -------------------- //
app.get('/department-info', (req, res) => {
    const departmentName = req.query.department_name;

    // 如果没有提供 departmentName，返回错误
    if (!departmentName) {
        return res.status(400).json({ error: 'Department Name is required' });
    }

    // 查询对应的 Department_ID
    const departmentQuery = `
        SELECT Department_ID 
        FROM department 
        WHERE Department_Name = ?`;

    // 首先查询 Department_ID
    DepartmentManagementDB.query(departmentQuery, [departmentName], (err, results) => {
        if (err || results.length === 0) {
            return res.status(500).json({ error: 'Error fetching department information or department not found' });
        }
        
        const departmentID = results[0].Department_ID;

        // 查询开发者和经理信息，关联部门表，获取开发者ID、经理ID和部门名称
        const developerQuery = `
            SELECT d.Developer_id, dm.Department_Name
            FROM developer_works_in d
            JOIN department dm ON d.Department_ID = dm.Department_ID
            WHERE d.Department_ID = ?`;

        const managerQuery = `
            SELECT m.Manager_id, dm.Department_Name
            FROM manager_works_in m
            JOIN department dm ON m.Department_ID = dm.Department_ID
            WHERE m.Department_ID = ?`;

        // 查询开发者ID
        DepartmentManagementDB.query(developerQuery, [departmentID], (err, developers) => {
            if (err) {
                return res.status(500).json({ error: 'Error fetching developers' });
            }

            // 查询经理ID
            DepartmentManagementDB.query(managerQuery, [departmentID], (err, managers) => {
                if (err) {
                    return res.status(500).json({ error: 'Error fetching managers' });
                }

                // 返回开发者和经理数据
                res.json({
                    developers: developers,  // 返回开发者列表，包括Developer_id和Department_Name
                    managers: managers       // 返回经理列表，包括Manager_id和Department_Name
                });
            });
        });
    });
});

// -------------------- 用户验证（verify-user） -------------------- //
app.post('/verify-user', (req, res) => {
    const { username } = req.body;

    if (!username) {
        return res.status(400).json({ success: false, message: 'Username is required' });
    }

    // 查询用户身份
    const queryDeveloper = "SELECT * FROM developer WHERE Developer_id = ?";
    employeeDB.query(queryDeveloper, [username], (err, results) => {
        if (err) {
            console.error('Error verifying user:', err);
            return res.status(500).json({ success: false, message: 'Server error' });
        }
        if (results.length > 0) {
            return res.json({ success: true, role: 'developer', username });
        }

        const queryManager = "SELECT * FROM manager WHERE Manager_id = ?";
        employeeDB.query(queryManager, [username], (err, results) => {
            if (err) {
                console.error('Error verifying user:', err);
                return res.status(500).json({ success: false, message: 'Server error' });
            }
            if (results.length > 0) {
                return res.json({ success: true, role: 'manager', username });
            } else {
                return res.status(404).json({ success: false, message: 'User not found' });
            }
        });
    });
});

app.get('/get-security-questions', (req, res) => {
    const username = req.query.username;

    if (!username) {
        return res.status(400).json({ success: false, message: 'Username is required' });
    }

    const query = "SELECT Question_1, Question_2, Question_3 FROM security_questions WHERE ID = ?";
    employeeDB.query(query, [username], (err, results) => {
        if (err) {
            console.error('Error fetching security questions:', err);
            return res.status(500).json({ success: false, message: 'Server error' });
        }

        if (results.length === 0) {
            return res.status(404).json({ success: false, message: 'No security questions found for this user' });
        }

        const questions = [results[0].Question_1, results[0].Question_2, results[0].Question_3].filter(q => q);
        res.json({ success: true, questions });
    });
});

app.post('/verify-security-answers', (req, res) => {
    const { username, answers } = req.body;

    if (!username || !answers || !Array.isArray(answers)) {
        return res.status(400).json({ success: false, message: 'Invalid request' });
    }

    const query = "SELECT Answer_1, Answer_2, Answer_3 FROM security_questions WHERE ID = ?";
    employeeDB.query(query, [username], (err, results) => {
        if (err) {
            console.error('Error verifying security answers:', err);
            return res.status(500).json({ success: false, message: 'Server error' });
        }

        if (results.length === 0) {
            return res.status(404).json({ success: false, message: 'No answers found for this user' });
        }

        const correctAnswers = [results[0].Answer_1, results[0].Answer_2, results[0].Answer_3].filter(a => a);
        const allCorrect = correctAnswers.every((answer, index) => answer === answers[index]);

        if (allCorrect) {
            res.json({ success: true });
        } else {
            res.json({ success: false, message: 'Incorrect answers' });
        }
    });
});

// -------------------- 根据用户ID获取部门信息并随机选择一个经理ID -------------------- //
app.get('/get-department-and-manager', (req, res) => {
    const userID = req.query.userID;

    if (!userID) {
        return res.status(400).json({ success: false, message: 'User ID is required' });
    }

    // 查询用户所属的部门，并获取该部门的所有经理ID
    const departmentQuery = `
        SELECT dm.Department_Name, m.Manager_id
        FROM developer_works_in d
        JOIN department dm ON d.Department_ID = dm.Department_ID
        JOIN manager_works_in m ON m.Department_ID = dm.Department_ID
        WHERE d.Developer_id = ?`;

    DepartmentManagementDB.query(departmentQuery, [userID], (err, results) => {
        if (err) {
            console.error('Error fetching department and manager information:', err);
            return res.status(500).json({ success: false, message: 'Server error' });
        }

        if (results.length === 0) {
            return res.status(404).json({ success: false, message: 'No department found for this user' });
        }

        // 从属于该部门的经理中随机选择一个
        const departmentName = results[0].Department_Name;
        const managerIDs = results.map(result => result.Manager_id);
        const randomManagerID = managerIDs[Math.floor(Math.random() * managerIDs.length)];

        res.json({
            success: true,
            department: departmentName,
            managerID: randomManagerID
        });
    });
});

//---------------------------------------更改密码----------------------------------------------//
app.post('/update-password', (req, res) => {
    const { username, role, newPassword } = req.body;

    if (!username || !role || !newPassword) {
        return res.status(400).json({ success: false, message: 'Invalid request data.' });
    }

    let updateQuery = '';
    if (role === 'developer') {
        updateQuery = 'UPDATE developer SET Developer_password = ? WHERE Developer_id = ?';
    } else if (role === 'manager') {
        updateQuery = 'UPDATE manager SET Manager_password = ? WHERE Manager_id = ?';
    } else {
        return res.status(400).json({ success: false, message: 'Invalid role specified.' });
    }

    // 执行更新操作
    employeeDB.query(updateQuery, [newPassword, username], (err, result) => {
        if (err) {
            console.error('Error updating password:', err);
            return res.status(500).json({ success: false, message: 'Failed to update password.' });
        }

        res.json({ success: true, message: 'Password updated successfully.' });
    });
});

// -------------------------------服务器端获取部门信息的 API-----------------------------------//
app.get('/get-position-by-manager', (req, res) => {
    const managerID = req.query.managerID;

    if (!managerID) {
        return res.status(400).json({ success: false, message: 'Manager ID is required' });
    }

    // 查询经理所属的部门职位信息，关联 manager_works_in 和 department 表
    const positionQuery = `
        SELECT dm.Department_Name
        FROM manager_works_in m
        JOIN department dm ON m.Department_ID = dm.Department_ID
        WHERE m.Manager_id = ?`;

    DepartmentManagementDB.query(positionQuery, [managerID], (err, results) => {
        if (err) {
            console.error('Error fetching department information:', err);
            return res.status(500).json({ success: false, message: 'Server error while fetching department information' });
        }

        if (results.length === 0) {
            return res.status(404).json({ success: false, message: 'No department found for this manager' });
        }

        res.json({ success: true, position: results[0].Department_Name });
    });
});

// -------------------------服务器端代码 - 获取下一个 Developer ID--------------------------//
app.get('/get-next-developer-id', (req, res) => {
    const query = 'SELECT Developer_id FROM developer ORDER BY Developer_id DESC LIMIT 1';

    employeeDB.query(query, (err, results) => {
        if (err) {
            console.error('Error fetching the last Developer ID:', err);
            return res.status(500).json({ success: false, message: 'Server error' });
        }

        if (results.length === 0) {
            // 如果数据库中没有开发人员记录，返回默认的 Developer ID
            return res.json({ success: true, nextDeveloperID: 'd00001' });
        }

        // 计算下一个 Developer ID
        const lastDeveloperID = results[0].Developer_id;
        const nextDeveloperID = 'd' + String(parseInt(lastDeveloperID.slice(1)) + 1).padStart(5, '0');

        res.json({ success: true, nextDeveloperID: nextDeveloperID });
    });
});

// -------------------------------------------创建搜索接口 ---------------------------------------------------------------//
app.get('/search', (req, res) => {
    const { id } = req.query;

    // 根据输入的 ID 查询项目或任务
    const query = `
        SELECT 
            p.Project_id, 
            p.task_id, 
            a.Manager_id, 
            e.Feedback_id, 
            e.Developer_id, 
            f.grade
        FROM 
            pro_task AS p
        LEFT JOIN 
            assi AS a ON p.task_id = a.task_id
        LEFT JOIN 
            evaluate AS e ON a.Manager_id = e.Manager_id
        LEFT JOIN 
            feedback AS f ON e.Feedback_id = f.Feedback_id
        WHERE 
            p.Project_id = ? OR p.task_id = ?
    `;

    // 执行查询并返回结果
    db.query(query, [id, id], (err, results) => {
        if (err) {
            console.error('Database query error:', err);
            return res.status(500).json({ error: 'Database query failed' });
        } else {
            res.json(results);
        }
    });
});

//---------------------------- Developer Start Task -------------------------------------//
app.get('/api/available-tasks', (req, res) => {
    const developerId = req.query.developer_id;

    const taskQuery = `
        SELECT t.task_id 
        FROM task t
        JOIN finish f ON t.task_id = f.task_id
        WHERE t.task_state = 'Standing by' AND f.developer_id = ?;
    `;
    
    projectTaskDB.query(taskQuery, [developerId], (err, results) => {
        if (err) {
            console.error('Error fetching tasks:', err);
            return res.status(500).send('Server error');
        }
        res.json(results);
    });
});

//-------------------------- Developer Start Task Change State---------------------------------//
app.post('/api/start-task', (req, res) => {
    const { task_id } = req.body;

    const updateTaskQuery = `
        UPDATE task
        SET task_state = 'In process'
        WHERE task_id = ? AND task_state = 'Standing by';
    `;

    projectTaskDB.query(updateTaskQuery, [task_id], (err, results) => {
        if (err) {
            console.error('Error updating task state:', err);
            return res.status(500).send('Server error');
        }
        res.json({ success: true, message: 'Task started successfully' });
    });
});

//---------------------------- Developer Start Task -------------------------------------//
app.get('/api/submit-tasks', (req, res) => {
    const developerId = req.query.developer_id;

    const taskQuery = `
        SELECT t.task_id 
        FROM task t
        JOIN finish f ON t.task_id = f.task_id
        WHERE t.task_state = 'In process' AND f.developer_id = ?;
    `;
    
    projectTaskDB.query(taskQuery, [developerId], (err, results) => {
        if (err) {
            console.error('Error fetching tasks:', err);
            return res.status(500).send('Server error');
        }
        res.json(results);
    });
});

//-------------------------- Developer Start Task Change State---------------------------------//
app.post('/api/submit-task', (req, res) => {
    const { task_id } = req.body;

    const updateTaskQuery = `
        UPDATE task
        SET task_state = 'Unevaluated'
        WHERE task_id = ? AND task_state = 'In process';
    `;

    projectTaskDB.query(updateTaskQuery, [task_id], (err, results) => {
        if (err) {
            console.error('Error updating task state:', err);
            return res.status(500).send('Server error');
        }
        res.json({ success: true, message: 'Task submitted successfully' });
    });
});

//-------------------------------修改个人信息-----------------------//
app.post('/update-user-info', (req, res) => {
    const { role, username, name, phoneNumber, education } = req.body;
    
    let updateQuery = '';
    
    // 根据 role 值来构建 SQL 更新语句
    if (role && role.toLowerCase() === 'developer') {
        updateQuery = `
            UPDATE developer 
            SET Developer_name = ?, PhoneNumber = ?, Education = ? 
            WHERE Developer_id = ?
        `;
    } else if (role && role.toLowerCase() === 'manager') {
        updateQuery = `
            UPDATE manager 
            SET Manager_name = ?, PhoneNumber = ?, Education = ? 
            WHERE Manager_id = ?
        `;
    } else {
        console.error("Invalid role provided: ", role);
        return res.status(400).json({ success: false, message: "Invalid role provided" });
    }

    // 打印日志以调试
    console.log("Role:", role);
    console.log("Update Query:", updateQuery);

    // 执行更新查询
    employeeDB.query(updateQuery, [name, phoneNumber, education, username], (error, results) => {
        if (error) {
            console.error('Error updating user data:', error);
            res.status(500).json({ success: false, message: "Database error occurred" });
        } else if (results.affectedRows === 0) {
            // 检查是否有行受影响，防止错误的用户 ID 导致更新失败
            console.warn('No rows updated. Please check username and role validity.');
            res.status(404).json({ success: false, message: "User not found or no changes made" });
        } else {
            res.json({ success: true, message: "User information updated successfully" });
        }
    });
});

// -------------------- 启动服务器 -------------------- //
app.listen(3001, () => {
    console.log('Server started on port 3001');
});
