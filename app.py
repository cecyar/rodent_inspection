import csv
import pickle
import psycopg2
import psycopg2.extras
import numpy as np
from flask import Flask, request, jsonify, render_template


database_uri = "postgresql://root:root@db:5432/rodent"


# Creamos Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config["DEBUG"] = True
conn = psycopg2.connect(database_uri)
cursor = conn.cursor()


# Crea base de datos inicial
tbl = "all_info"
cursor.execute('DROP TABLE IF EXISTS all_info')
cursor.execute('CREATE TABLE all_info ('
               'job_ticket_or_work_order_id integer DEFAULT NULL,'
               'job_id varchar DEFAULT NULL,'
               'inspection_type varchar DEFAULT NULL,'
               'boro_code integer DEFAULT NULL,'
               'zip_code integer DEFAULT NULL,'
               'latitude float DEFAULT NULL,'
               'longitude float DEFAULT NULL,'
               'inspection_date varchar DEFAULT NULL,'
               'result varchar DEFAULT NULL)')

with open('data/test.csv', 'r') as f:   # with open('data/Rodent_Inspection.csv', 'r') as f:
    reader_all = csv.reader(f)
    columns = next(reader_all)
    cursor.execute("SELECT * FROM all_info")
    datos = cursor.fetchall()
    query = 'insert into all_info({0}) values ({1})'
    query = query.format(','.join(columns), ','.join(['%s'] * len(columns)))
    for data in reader_all:
        cursor.execute(query, data)
    cursor.execute("SELECT * FROM all_info")
    datos = cursor.fetchall()
    conn.commit()


# Cargar Modelo para predicciones
with open("data/entrenamiento_lr.pkl", "rb") as f:
    model_loaded = pickle.load(f)


# Página de inicio
@app.route('/main')
def index():
    return render_template('index.html')


# Mostrar base de datos
@app.route('/show_all', methods=['GET'])
def show_all():
    cursor.execute("SELECT * FROM all_info")
    results = cursor.fetchall()
    conn.commit()

    return render_template('show_all.html', data=results)


# Hacer predicción para un registro, GET
@app.route('/prediction', methods=['GET'])
def feed_data():
    return render_template('prediction.html')


# Hacer predicción para un registro, POST
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


# Agregar un registro, GET
@app.route('/add_register', methods=['GET'])
def get_data():
    return render_template('add_register.html')


# Agregar un registro, POST
@app.route('/add_register', methods=['POST'])
def add_register():
    array_inputs = np.array([request.form['job_ticket_or_work_order_id'],
                             request.form['job_id'],
                             request.form['inspection_type'],
                             request.form['boro_code'],
                             request.form['zip_code'],
                             request.form['latitude'],
                             request.form['longitude'],
                             request.form['inspection_date'],
                             request.form['result']])
    cursor.execute("INSERT INTO all_info ("
                   "job_ticket_or_work_order_id,"
                   "job_id,"
                   "inspection_type,"
                   "boro_code,"
                   "zip_code,"
                   "latitude,"
                   "longitude,"
                   "inspection_date,"
                   "result) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (array_inputs[0],
                    array_inputs[1],
                    array_inputs[2],
                    array_inputs[3],
                    array_inputs[4],
                    array_inputs[5],
                    array_inputs[6],
                    array_inputs[7],
                    array_inputs[8]), )
    cursor.execute("SELECT * FROM all_info")
    results = cursor.fetchall()
    conn.commit()
    res_val = array_inputs
    return render_template('add_register.html', triptype_val=res_val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)