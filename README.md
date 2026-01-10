<h1>Task Tracker CLI</h1>
<p>A lightweight Command Line Interface (CLI) application built with Python to efficiently manage and track daily tasks. Tasks are persisted locally using a JSON file.</p>
https://github.com/Arunima-2232/task_tracker_cli/blob/main/task%20tracker%20cli/images/Screenshot%202026-01-10%20232956.png
https://github.com/Arunima-2232/task_tracker_cli/blob/main/task%20tracker%20cli/images/Screenshot%202026-01-10%20233109.png
<br><p>Taken from: https://roadmap.sh/projects/task-tracker</p>
<h3>How to run:</h3>
<p>On command prompt run pip install -e "PATH"</p>
<h3>Features</h3>
<ul>
  <li>Add tasks</li>
  <li>Delete tasks</li>
  <li>Update existing tasks</li>
  <li>View all tasks</li>
  <li>View completed tasks</li>
  <li>View pending tasks</li>
  <li>Mark tasks as completed</li>
</ul>
<h3>How It Works</h3>
<ul>
  <li>All tasks are stored locally in a JSON file named data.json</li>
  <li>The file is created if it doesn't exist.</li>
  <li>Each task maintains essential metadata to ensure traceability and updates.</li>
</ul>
<h3>Task Schema</h3>
<p>Each task in data.json contains:</p>
<code>
  {
  "id": 1,
  "task_name": "Finish README",
  "status": "done / not done",
  "created_at": "dd-mm-yyyy hh-mm",
  "updated_at": "dd-mm-yyyy hh-mm"
}
</code>
<h2>Why This Porject?</h2>
<p>This project demonstrates:</p>
<ul>
  <li>Practical use of file handling in Python</li>
  <li>Working with JSON for persistent storage</li>
  <li>Implementing CRUD operations</li>
</ul>
