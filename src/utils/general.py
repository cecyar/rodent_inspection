import yaml

def read_yaml(credentials_file):
    """
    Descarga yaml para importar las credenciales.
    """
    config = None
    try:
        with open (credentials_file, 'r') as f:
            config = yaml.safe_load(f)
    except:
        raise FileNotFoundError('Could not load the file')
    return config
    

def get_api_token(credentials_file):
    """
        Esta función recibe como parámetro:
            credentials_file: archivo generado por read_yaml.
        Y regresa:
            token: el token para comunicarse con la API.
        """
    token=read_yaml(credentials_file)['rodent_inspections']
    return token