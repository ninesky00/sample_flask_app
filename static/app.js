// static/app.js

function addTask() {
  var taskName = document.getElementById('taskName').value;
  if (taskName.trim() === '') {
      alert('Task name cannot be empty');
      return;
  }

  fetch('/add', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'task_name=' + encodeURIComponent(taskName),
  })
  .then(response => response.json())
  .then(data => {
      if (data.result === 'success') {
          window.location.reload();
      } else {
          alert('Failed to add task');
      }
  });
}

function deleteTask(taskId) {
  fetch('/delete/' + taskId, {
      method: 'DELETE',
  })
  .then(response => response.json())
  .then(data => {
      if (data.result === 'success') {
          window.location.reload();
      } else {
          alert('Failed to delete task');
      }
  });
}
