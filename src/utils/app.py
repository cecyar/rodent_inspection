import csv
import psycopg2.extras
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import SQLALCHEMY_DATABASE_URI


database_uri = "postgresql://root:root@db:5432/rodent"


# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri     # SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = True
conn = psycopg2.connect(database_uri)
db = SQLAlchemy(app)
ma = Marshmallow(app)





@app.route('/home', methods=['GET'])
def home():
    """
    Function to upload csv file to sqlserver and show on api
    """
    tbl = "api_model"
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS api_model')
    cursor.execute('CREATE TABLE api_model (job_ticket_or_work_order_id integer DEFAULT NULL,job_id varchar DEFAULT '
                   'NULL,inspection_type varchar DEFAULT NULL,boro_code integer DEFAULT NULL,zip_code integer DEFAULT '
                   'NULL,latitude float DEFAULT NULL,longitude float DEFAULT NULL,inspection_date varchar DEFAULT '
                   'NULL,result varchar DEFAULT NULL)')

    with open('Rodent_Inspection.csv', 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        cursor.execute("SELECT * FROM api_model")
        datos = cursor.fetchall()
        query = 'insert into api_model({0}) values ({1})'
        query = query.format(','.join(columns), ','.join(['%s'] * len(columns)))
        for data in reader:
            cursor.execute(query, data)
        cursor.execute("SELECT * FROM api_model")
        datos = cursor.fetchall()
        conn.commit()

    return render_template('home.html', data=datos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")


class Task(db.Model):
    job_ticket_or_work_order_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Text)
    inspection_type = db.Column(db.Text)
    boro_code = db.Column(db.Integer)
    zip_code = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    inspection_date = db.Column(db.DateTime)
    result = db.Column(db.Text)

    def __init__(self, job_id, inspection_type, boro_code, zip_code, latitude, longitude, inspection_date, result):
        self.job_id = job_id
        self.inspection_type = inspection_type
        self.boro_code = boro_code
        self.zip_code = zip_code
        self.latitude = latitude
        self.longitude = longitude
        self.inspection_date = inspection_date
        self.result = result


db.create_all()


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("job_ticket_or_work_order_id", "job_id", "inspection_type", "boro_code", "zip_code", "latitude", "longitude", "inspection_date", "result")


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)