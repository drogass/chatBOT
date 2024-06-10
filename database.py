import sqlite3

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       task TEXT NOT NULL,
                       username TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_task(user_id, username, task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, username) VALUES (?, ?)', (task, username))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task, username FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
