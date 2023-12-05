from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sqlite3

DATABASE = "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.debug = True
CORS(app)


@app.route("/add_student", methods=["POST"])
@cross_origin()
def add_record():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
        INSERT INTO STUDENT (ADMISSION_NUMBER,FIRST_NAME, LAST_NAME,PHONE_NUMBER,HOSTEL_ID,ROOM_ID,SCHOOL_ID)
        VALUES (?, ?,?,?,?,?,?)
    """,
            (
                data["admissionNumber"],
                data["firstName"],
                data["lastName"],
                data["phoneNumber"],
                data["hostel"],
                data["roomNumber"],
                data["schoolId"],
            ),
        )
        conn.commit()
        message = "Record added successfully!"
    except sqlite3.Error as e:
        message = f"Database error: {e}"
    except Exception as e:
        message = f"Exception in _query: {e}"
    finally:
        conn.close()
    return jsonify({"message": message})


@app.route("/get_students", methods=["GET"])
def get_students():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    students = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(students)


@app.route("/update_student", methods=["PUT"])
def update_student():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
      UPDATE STUDENTS
      SET column1 = ?, column2 = ?
      WHERE id = ?
  """,
        (data["field1"], data["field2"], data["id"]),
    )
    conn.commit()
    conn.close()
    return "Record updated successfully!"


@app.route("/delete_student", methods=["DELETE"])
def delete_student():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
      DELETE FROM STUDENTS
      WHERE id = ?
  """,
        (data["id"],),
    )
    conn.commit()
    conn.close()
    return "Record deleted successfully!"
