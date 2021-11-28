import pandas as pd
import os
import src.utils.constants as constants

from sodapy import Socrata
from src.utils.general import *

token=get_api_token('conf/local/credentials.yaml')['api_token']

client = Socrata(constants.url_api, token)

results = client.get(constants.id_data_set, limit=constants.limite_api)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)