from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

db = sqlite3.connect('data.db')
cur = db.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    group TEXT);
    """)
db.commit()

cur.execute(""" INSERT INTO students(id, name, group)
VALUES('001', 'Emily', 'БИВТ-11')""")
db.commit()

class Student(BaseModel):
    id: int
    name: str
    grope: str

app = FastAPI()

@app.post("/student/add/")
async def student(student: Student):

    db = sqlite3.connect('data.db')
    cur = db.cursor()

    student_name = input('name: ')
    student_id = input('id: ')
    student_groupe = input('group: ')

    if cur.fetchone() is None:
        cur.execute(f"""INSERT INTO student VALUES (?, ?, ?)""", (student_id, student_name, student_groupe))
        db.commit()
        print('signin')
    else:
        print("there is a student whith the same id")
    db.commit()
    return student

@app.put("/student/update/")
async def update(student: Student):

    db = sqlite3.connect('data.db')
    cur = db.cursor()

    student_id = input('id: ')
    cur.execute("""UPDATE students SET group = ? WHERE id = stident_id""")
    db.commit()
    print('saved')
    db.commit()
    return(student)

@app.get("/student/{student_id}/")
async def get_id():

    db = sqlite3.connect('data.db')
    cur = db.cursor()

    i_d = input('id: ')

    cur.execute(""" SELECT * FROM students WHERE id = ? """, (i_d))
    rec = cur.fetchone()
    print("student's id:", i_d)
    print('name:', rec[0])
    print('group:', rec[1])
    cur.close()
    

@app.get("/students/all/")
async def get_all():

    db = sqlite3.connect('data.db')
    cur = db.cursor()

    cur.execute(""" SELECT * FROM students""")
    rec1 = cur.fetchall()
    for i in rec1:
        print("id:", i[0])
        print("name:", i[1])
        print("group:", i[2], end='\n\n')
    cur.close()
    












