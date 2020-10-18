import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

def get_todo_all():
    sql = 'select * from todo'
    cursor.execute(sql)
    result = list(cursor.fetchall())
    return result

def get_todo_not_complete():
    sql = 'select * from todo where is_complete=?'
    cursor.execute(sql, (0,))
    result = list(cursor.fetchall())
    return result

def get_todo_complete():
    sql = 'select * from todo where is_complete=?'
    cursor.execute(sql, (1,))
    result = list(cursor.fetchall())
    return result

def insert_todo(contents, category):
    sql = "insert into todo (contents, category, is_complete, complete_date) \
           values (?, ?, 0, null)"
    cursor.execute(sql, (contents, category))
    conn.commit()

def delete_todo(id):
    sql = 'delete from todo where id=:id'
    cursor.execute(sql, {'id': id})
    conn.commit()

def complete_todo(id, complete_date):
    sql = 'update todo set is_complete=1, complete_date=date(?) where id=?'
    cursor.execute(sql, (complete_date, id))
    conn.commit()

def undo_complete_todo(id):
    sql = 'update todo set is_complete=0, complete_date=null where id=?'
    cursor.execute(sql, (id,))
    conn.commit()