import src.utils.constants as constants
#import pickle

from sodapy import Socrata
from src.utils.general import *


# Obtiene el token generado para poder descargar la informacion
token=get_api_token('conf/local/credentials.yaml')['api_token']

client = Socrata(constants.url_api, token)
data = client.get(constants.id_data_set, limit=constants.limite_api)
#data_pkl = pickle.dumps(data)

# Convert to pandas DataFrame
#data_df = pd.DataFrame.from_records(data)