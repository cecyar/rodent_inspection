# coding=utf-8
import yaml
import logging
import psycopg2


logging.basicConfig(level=logging.INFO)


def read_yaml(credentials_file):
    """
    Descarga yaml para importar las credenciales.
    """
    config = None
    try:
        with open(credentials_file, 'r') as f:
            config = yaml.safe_load(f)
    except:
        logging.warning("No se pudo leer el archivo yaml")
        raise FileNotFoundError("No se pudo leer el archivo")

    return config
    

def get_api_token(credentials_file):
    """
    Esta función recibe como parámetro:
        credentials_file: archivo generado por read_yaml.
    Y regresa:
        token: el token para comunicarse con la API.
    """
    logging.info("Leyendo las credenciales de {}".format(credentials_file))
    token = read_yaml(credentials_file)['rodent_inspections']

    return token


def get_db_conn_sql_alchemy(credenciales):
    """Get credentials for db connection"""
    creds = read_yaml(credenciales)['db']

    connection = "postgresql://{}:{}@{}:{}/{}".format(creds['user'], creds['pass'], creds['host'], creds['port'],
                                                      creds['db'])

    return connection


def get_db_conn_psycopg(credentials_file):
    """
    """
    creds = read_yaml(credentials_file)['db']

    connection = psycopg2.connect(
        user=creds['user'],
        password=creds['pass'],
        host=creds['host'],
        port=creds['port'],
        database=creds['db']
    )

    return connection