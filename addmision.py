from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
import sqlite3
from datetime import datetime, timedelta

router = APIRouter()  # <--- Ye variable 'router' hona chahiye

@router.post("/submit_admission")
async def submit_admission(
    name: str = Form(...), dad_name: str = Form(...), contact: str = Form(...),
    admission_date: str = Form(...), student_class: str = Form(..., alias="class")
):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, dad_name, contact, admission_date, class) VALUES (?,?,?,?,?)",
                   (name, dad_name, contact, admission_date, student_class))
    student_id = cursor.lastrowid
    conn.commit()
    conn.close()

    # Fee Record
    due_date = datetime.strptime(admission_date, "%Y-%m-%d") + timedelta(days=30)
    conn2 = sqlite3.connect("sf_manager.db")
    conn2.execute("INSERT INTO fee_records (student_id, amount, due_date, status) VALUES (?, 5000, ?, 'Pending')",
                  (student_id, due_date.strftime("%Y-%m-%d")))
    conn2.commit()
    conn2.close()
    return RedirectResponse(url="/", status_code=303)