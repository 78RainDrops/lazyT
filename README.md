# 📝 lazyT – A Simple CLI Todo List

`lazyT` is a lightweight **command-line todo list manager** written in Python.  
It lets you quickly add, edit, update, view, and delete tasks directly from your terminal.  
All tasks are stored in a local JSON file in your home directory (`~/.lazyT_tasks.json`), so your data persists between sessions.  

---

## 🚀 Features  
- ➕ Add new tasks with timestamps  
- 📋 List tasks (filter by status: `todo`, `in-progress`, `done`)  
- ✏️ Edit existing task descriptions  
- ✅ Update task status (mark as `in-progress` or `done`)  
- ❌ Delete tasks  
- 💾 Persistent storage using JSON  

---

## 📂 Project Structure  

```
lazy-folder/        # Root project folder
├── .gitignore      # Ignore venv, cache, JSON storage
├── setup.py        # Packaging & entry point setup
├── requirements.txt # Optional dependencies
├── README.md       # Project documentation
├── lazy_task/      # Main Python package
│   ├── __init__.py
│   ├── lazy.py     # CLI logic & commands
│   └── save_task.py # Task persistence (JSON)
└── tests/
    └── test_lazy.py # Unit tests
```

---

## 🛠️ Installation  

### Prerequisites  
- Python **3.8+** (tested on 3.13 as well)  
- `pip` package manager  

### Install  
Clone the repo and install it as a package:  

```bash
git clone https://github.com/78RainDrops/lazy-folder.git
cd lazy-folder
pip install .
```

This will register the CLI command `lazyT` in your environment.  

---

## ▶️ Usage  

Run the CLI with:  

```bash
lazyT [command] [options]
```

### Available Commands  

| Command | Description | Example |
|---------|-------------|---------|
| `add <task>` | Add a new task | `lazyT add "Buy groceries"` |
| `list` | Show all tasks | `lazyT list` |
| `list -s <status>` | Filter tasks by status (`todo`, `in-progress`, `done`) | `lazyT list -s done` |
| `edit <id> <new description>` | Edit a task’s description | `lazyT edit 2 "Buy milk and bread"` |
| `task <id> -s <status>` | Update a task’s status | `lazyT task 2 -s done` |
| `del <id>` | Delete a task | `lazyT del 2` |

---

## 📖 Examples  

```bash
# Add tasks
lazyT add "Finish README"
lazyT add "Push code to GitHub"

# List tasks
lazyT list
lazyT list -s todo

# Edit a task
lazyT edit 1 "Finish and polish README"

# Mark as done
lazyT task 1 -s done

# Delete a task
lazyT del 2
```

Output example for `lazyT list`:  

```
ID    TASK                 STATUS       CREATED              UPDATED
----------------------------------------------------------------------------
1     Finish README        done         2025-09-15 | 22:00   2025-09-15 | 22:05
```

---

## 🧪 Testing  

To run unit tests:  

```bash
pytest tests/
```

---

## 🤝 Contributing  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m 'Add feature'`)  
4. Push (`git push origin feature-name`)  
5. Open a Pull Request  

---

## 📜 License  

MIT License © 2025 [78RainDrops](https://github.com/78RainDrops)  
