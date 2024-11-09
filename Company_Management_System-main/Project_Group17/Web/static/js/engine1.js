    // Function to load project data from localStorage and display it
    function loadProjectData() {
        let projects = JSON.parse(localStorage.getItem('projects')) || []; // Load all projects from localStorage
        
        if (projects.length > 0) {
            const activityContainer = document.getElementById('activityReports');
            activityContainer.innerHTML = ''; // Clear previous content

            // Iterate over the projects array and generate HTML structure for each project
            projects.forEach(project => {
                const projectReport = document.createElement('div');
                projectReport.classList.add('activity-report');
                projectReport.innerHTML = `
                    <h2>Establish Project Successfully! - Assign</h2>
                    <p><strong>Project ID:</strong> ${project.projectID}</p>
                    <p><strong>Project Name:</strong> ${project.projectName}</p>
                    <p><strong>Task ID:</strong> ${project.tasks.map(task => task.taskID).join(', ')}</p>
                    <p><strong>Task Name:</strong> ${project.tasks.map(task => task.taskName).join(', ')}</p>
                `;
                activityContainer.appendChild(projectReport);
            });
        } else {
            const activityContainer = document.getElementById('activityReports');
            const noProjectMessage = document.createElement('p');
            noProjectMessage.innerText = "No projects found. Please establish a project first.";
            activityContainer.appendChild(noProjectMessage);
        }
    }

    // Call the function on page load
    window.onload = function() {
        loadProjectData();
    };
