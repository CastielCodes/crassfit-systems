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


@app.route("/add_hostel", methods=["POST"])
@cross_origin()
def add_hostel():
   data = request.get_json()
   conn = get_db()
   cursor = conn.cursor()
   try:
       cursor.execute(
           """
       INSERT INTO HOSTEL (HOSTEL_ID,HOSTEL_NAME,NO_OF_ROOMS,LANDLORD_ID,NO_OF_STUDENTS,SCHOOL_ID)
       VALUES (?,?,?,?,?,?)
   """,
           (
               data["hostelId"],
               data["hostelName"],
               data["numberOfRooms"],
               data["landlordId"],
               data["numberofStudents"],
               data["schoolId"],
           ),
       )
       conn.commit()
       message = "Record added successfully!"
   except sqlite3.Error as e:
       message = f"Database error: {e}"
       print(e)
   except Exception as e:
       message = f"Exception in _query: {e}"
       print(e)
   finally:
       conn.close()
   return jsonify({"message": message})

@app.route("/get_hostels", methods=["GET"])
def get_hostels():
   conn = get_db()
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM HOSTEL")
   hostels = [dict(row) for row in cursor.fetchall()]
   conn.close()
   return jsonify(hostels)


@app.route("/get_rooms", methods=["GET"])
def get_rooms():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM ROOM")
  rooms = [dict(row) for row in cursor.fetchall()]
  conn.close()
  return jsonify(rooms)


@app.route("/add_room", methods=["POST"])
@cross_origin()
def add_room():
  data = request.get_json()
  conn = get_db()
  cursor = conn.cursor()
  try:
      cursor.execute(
          """
      INSERT INTO ROOM (ROOM_ID,HOSTEL_ID,STATUS,PRICE,ROOM_NUMBER,SCHOOL_ID)
      VALUES (?, ?,?,?,?,?)
  """,
          (
              data["roomId"],
              data["hostelId"],
              data["status"],
              data["price"],
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



@app.route("/get_schools", methods=["GET"])
def get_schools():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM SCHOOL")
  rooms = [dict(row) for row in cursor.fetchall()]
  conn.close()
  return jsonify(rooms)


@app.route("/add_school", methods=["POST"])
@cross_origin()
def add_school():
 data = request.get_json()
 conn = get_db()
 cursor = conn.cursor()
 try:
     cursor.execute(
         """
     INSERT INTO SCHOOL (SCHOOL_ID,SCHOOL_NAME,NO_OF_STAFF,NO_OF_STUDENTS,SCHOOL_LOCATION)
     VALUES (?, ?,?,?,?)
 """,
         (
             data["schoolId"],
             data["schoolName"],
             data["staffNumber"],
             data["studentNumber"],
             data["location"],
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




@app.route("/get_staff", methods=["GET"])
def get_staff():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM STAFF")
  rooms = [dict(row) for row in cursor.fetchall()]
  conn.close()
  return jsonify(rooms)



@app.route("/add_staff", methods=["POST"])
@cross_origin()
def add_staff():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO STAFF (STAFF_NUMBER, FIRST_NAME, LAST_NAME, STAFF_POSITION, SCHOOL_ID)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["staffNo"],
                data["firstName"],
                data["lastName"],
                data["position"],
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



@app.route("/get_landlords", methods=["GET"])
def get_landlords():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LANDLORD")
    landlords = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(landlords)

@app.route("/add_landlord", methods=["POST"])
@cross_origin()
def add_landlord():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO LANDLORD (LANDLORD_ID, FIRST_NAME, LAST_NAME, PHONE_NUMBER, NATIONAL_ID)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["landlordId"],
                data["firstName"],
                data["lastName"],
                data["phoneNumber"],
                data["nationalId"],
                
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