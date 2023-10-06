import sqlite3
from meta.singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    _db = None

    def __init__(self) -> None:
        if not self._db:
            self._db = self.create_connection()

    def create_connection(self):
        db = sqlite3.connect("todo.db", check_same_thread=False)
        c = db.cursor()
        c.execute(
            """
                CREATE TABLE IF NOT EXISTS tasks
                (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    create_at TEXT NOT NULL
                )
            """
        )
        db.commit()
        return db

    def get_all_tasks(self):
        c = self._db.cursor()
        c.execute("SELECT * FROM tasks")
        records = c.fetchall()
        self._db.commit()
        return records

    def insert_task(self, values):
        c = self._db.cursor()
        c.execute("Insert INTO tasks (task, create_at) VALUES (?,?)", values)
        id = c.lastrowid
        self._db.commit()
        return id

    def delete_task(self, task_id):
        c = self._db.cursor()
        c.execute(
            f"DELETE FROM tasks WHERE id={task_id}",
        )
        self._db.commit()

    def update_task(self, task_id, task_description):
        c = self._db.cursor()
        c.execute("UPDATE tasks SET task=? WHERE id=?", (task_description, task_id))
        self._db.commit()
