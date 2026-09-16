from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from database import get_db

app = FastAPI(title="Skill Rise Admission")

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# =========================
# ADMISSION FORM
# =========================

@app.get("/", response_class=HTMLResponse)
async def admission_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admission.html"
    )


# =========================
# SAVE ADMISSION
# =========================

@app.post("/submit_admission")
async def submit_admission(
    name: str = Form(...),
    dad_name: str = Form(...),
    father_profession: str = Form(""),
    mother_name: str = Form(""),
    contact: str = Form(""),
    emergency_phone: str = Form(""),
    course: str = Form(""),
    hobby: str = Form(""),
    weight: str = Form(""),
    height: str = Form(""),
    dob: str = Form(""),
    blood_group: str = Form(""),
    admission_date: str = Form(...)
):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO admissions (
            name,
            dad_name,
            father_profession,
            mother_name,
            contact,
            emergency_phone,
            course,
            hobby,
            weight,
            height,
            dob,
            blood_group,
            admission_date
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
        """,
        (
            name,
            dad_name,
            father_profession,
            mother_name,
            contact,
            emergency_phone,
            course,
            hobby,
            weight,
            height,
            dob if dob else None,
            blood_group,
            admission_date
        )
    )

    db.commit()

    cursor.close()
    db.close()

    return RedirectResponse(
        url="/list",
        status_code=303
    )


# =========================
# VIEW ALL ADMISSIONS
# =========================

@app.get("/list", response_class=HTMLResponse)
async def admission_list(request: Request):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT *
        FROM admissions
        ORDER BY id DESC
        """
    )

    admissions = cursor.fetchall()

    cursor.close()
    db.close()

    return templates.TemplateResponse(
        request=request,
        name="list.html",
        context={
            "admissions": admissions
        }
    )


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8001
    )