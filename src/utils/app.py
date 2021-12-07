import csv
import pickle
import psycopg2
import psycopg2.extras
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


database_uri = "postgresql://root:root@db:5432/rodent"


# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri     # SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = True
conn = psycopg2.connect(database_uri)


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


# Cargar Modelo
with open("entrenamiento_lr.pkl", "rb") as f:
    model_loaded = pickle.load(f)


@app.route('/prediction', methods=['GET'])
def feed_data():
    return render_template('prediction.html')


@app.route('/prediction', methods=['POST'])
def predict():
    array_inputs = np.array([request.form['job_id'],
                             request.form['boro_code'],
                             request.form['zip_code'],
                             request.form['latitude'],
                             request.form['longitude'],
                             request.form['1'],
                             request.form['2'],
                             request.form['3'],
                             request.form['4'],
                             request.form['5']]).reshape(-1, 1).T
    res_val = model_loaded.predict(array_inputs)
    return render_template('prediction.html', triptype_val=res_val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)