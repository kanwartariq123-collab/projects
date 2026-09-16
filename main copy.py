import sys
from pathlib import Path

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

# Allow Python to find database.py in ~/studentportal
sys.path.insert(0, str(PROJECT_DIR))


# ============================================================
# FASTAPI IMPORTS
# ============================================================

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database import get_db

import psycopg2


# ============================================================
# APP
# ============================================================

app = FastAPI(title="Skill Rise Admission System")


# ============================================================
# TEMPLATES
# ============================================================

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# ============================================================
# STATIC FILES
# ============================================================

STATIC_DIR = PROJECT_DIR / "static"

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)


# ============================================================
# HOME / ADMISSION FORM
# ============================================================

@app.get("/", response_class=HTMLResponse)
async def admission_form(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="admission.html"
    )


# ============================================================
# SAVE ADMISSION
# ============================================================

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

    try:

        cursor.execute(
            """
            INSERT INTO admissions
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
                dob,
                blood_group,
                admission_date
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                NULLIF(%s, '')::DATE,
                %s,
                %s
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
                dob,
                blood_group,
                admission_date
            )
        )

        db.commit()

    except Exception as e:

        db.rollback()

        print("ERROR SAVING ADMISSION:")
        print(e)

        return HTMLResponse(
            content=f"""
            <html>
            <body style="
                font-family: Arial;
                background:#f5f5f5;
                padding:50px;
                text-align:center;
            ">

                <h1 style="color:red;">
                    Admission Error
                </h1>

                <p>
                    {e}
                </p>

                <a href="/">
                    ← Back to Admission Form
                </a>

            </body>
            </html>
            """,
            status_code=500
        )

    finally:

        cursor.close()
        db.close()

    return RedirectResponse(
        url="/list",
        status_code=303
    )


# ============================================================
# VIEW ALL ADMISSIONS
# ============================================================

@app.get("/list", response_class=HTMLResponse)
async def admission_list(request: Request):

    db = get_db()
    cursor = db.cursor()

    try:

        cursor.execute(
            """
            SELECT *
            FROM admissions
            ORDER BY id DESC
            """
        )

        admissions = cursor.fetchall()

    finally:

        cursor.close()
        db.close()

    return templates.TemplateResponse(
        request=request,
        name="list.html",
        context={
            "request": request,
            "admissions": admissions
        }
    )


# ============================================================
# DELETE ADMISSION
# ============================================================

@app.post("/delete/{student_id}")
async def delete_admission(student_id: int):

    db = get_db()
    cursor = db.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM admissions
            WHERE id = %s
            """,
            (student_id,)
        )

        db.commit()

    except Exception as e:

        db.rollback()

        print("ERROR DELETING ADMISSION:")
        print(e)

    finally:

        cursor.close()
        db.close()

    return RedirectResponse(
        url="/list",
        status_code=303
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8001
    )