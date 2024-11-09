function goToRegistration(event) {
    event.preventDefault();
    const managerID = localStorage.getItem('managerID');
    if (!managerID) {
        alert('Manager ID is missing. Please login again.');
        return;
    }
    window.location.href = `registration.html?managerID=${encodeURIComponent(managerID)}`;
}

function performSearch() {
    const id = document.getElementById('searchID').value;
    fetch(`http://localhost:3001/search?id=${id}`)
        .then(response => response.json())
        .then(data => {
            const activityContainer = document.getElementById('activityReports');
            activityContainer.innerHTML = '';
            if (data.length > 0) {
                data.forEach(item => {
                    const projectReport = document.createElement('div');
                    projectReport.classList.add('activity-report');
                    projectReport.innerHTML = `
                        <h2>ProjectID: ${item.Project_id}</h2>
                        <p><strong>TaskID:</strong> ${item.task_id}</p>
                        <p><strong>ManagerID:</strong> ${item.Manager_id}</p>
                        <p><strong>DeveloperID:</strong> ${item.Developer_id}</p>
                        <p><strong>FeedbackID:</strong> ${item.Feedback_id}</p>
                        <p><strong>Grade:</strong> ${item.grade}</p>
                    `;
                    activityContainer.appendChild(projectReport);
                });
            } else {
                activityContainer.innerHTML = `<p>没有找到与ID ${id}相关的记录。</p>`;
            }
        })
        .catch(error => console.error('获取数据时出错:', error));
}
