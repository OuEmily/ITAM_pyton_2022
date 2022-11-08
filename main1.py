#черновик
app = FastAPI()
db = sqlite3.connect('data.db')
cur = db.cursor()

cur.execute(""" CREATE TABEL IF NOT EXISTS students (
    name TEXT,
    id INTEGER,
    group TEXT
)""")
db.commit()

student_name = input('name: ')
student_id = input('id: ')
student_groupe = input('groupe: ')

sql.execute('SELECT id FROM student')
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO student VALUES (?, ?, ?)", (student_id, student_name, student_groupe))
    db.commit()
    print('signin')
else:
    print("there is a student whith the same id")


class Student(BaseModel):
    id: int
    name: str
    group: str

@app.post("/student/add/")
def add_student(student: Student):
    print(student)
    with open('data.db', 'r', encoding='utf-8') as file:
        data = db.load()
    data[student.id] = student.name + student.group
    with open('data.db', 'w', encoding='utf-8') as file:
        db.dump(data, file)
    return 'saved'

@app.put("/student/update/")
def add_student(student: Student):
    print(student)
    with open('data.db', 'r', encoding='utf-8') as file:
        data = db.load()
    data[student.id] = student.name + student.group
    with open('data.db', 'w', encoding='utf-8') as file:
        db.dump(data, file)
    return 'saved'




        




