from flask import Flask, request
import oracledb

username = "SYSTEM"
userpwd = "123456789"
host = "localhost"
port = 1521
service_name = "orclpdb"

dsn = f"{username}/{userpwd}@{host}:{port}/{service_name}"
connection = oracledb.connect(dsn)


app = Flask(__name__)


def add_record():
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO STUDENTS (column1, column2)
        VALUES (:1, :2)
    """,
        (data["field1"], data["field2"]),
    )
    connection.commit()
    return "Record added successfully!"
