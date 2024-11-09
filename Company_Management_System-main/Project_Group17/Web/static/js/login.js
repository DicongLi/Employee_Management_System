// login.js
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const loginData = {
        username: username,
        password: password
    };

    fetch('http://localhost:3001/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            localStorage.setItem('userRole', data.role);
            localStorage.setItem('username', username);

            if (data.role === 'manager') {
                localStorage.setItem('managerID', data.managerID);
                window.location.href = 'manager.html';
            } else if (data.role === 'developer') {
                window.location.href = 'developer.html';
            }
        } else {
            document.getElementById('password').value = '';
            alert('Password or ID is incorrect');
        }
    })
    .catch(error => console.error('Error:', error));
});
