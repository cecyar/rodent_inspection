# coding=utf-8
import constants
#import pickle
from sodapy import Socrata
from general import *
from populate.populate import insert_inspection


wanted_columns=['inspection_type', 'result']
# Obtiene el token generado para poder descargar la informacion
token=get_api_token('credentials.yaml')['api_token']


def download_data(page):
    client = Socrata(constants.url_api, token)
    data = client.get(constants.id_data_set, limit=constants.limite_api)#, page=page)
    return data


# Convert to pandas DataFrame
def table_inspection(data):
    for row in data:
        info = {}
        for colum in wanted_columns:
            info[colum] = row.get(colum, '')

        info['latitude'] = row.get('location', {}).get('latitude', '')
        info['longitude'] = row.get('location', {}).get('longitude', '')

        insert_inspection(info)


def populate_everything():
    total_pages = 10000
    for page in range(total_pages):
        data = download_data(page)
        table_inspection(data)