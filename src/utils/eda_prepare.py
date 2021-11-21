def tit(col):
    return col.lower().replace('/', '_').replace(' ', '_').replace('ñ', 'n')

def clean_column(data):
    data.rename(columns={col: tit(col) for col in data.columns.values}, inplace=True)
    return data

def changeType_date(df):
    df['inspection_date'] = pd.to_datetime(df['inspection_date'])
    df['approved_date'] = pd.to_datetime(df['approved_date'])
    return df

def lowercase(df):
    df['inspection_type'] = df.inspection_type.str.lower()
    df['street_name'] = df.street_name.str.lower()
    #df['result'] = df.result.str.lower()
    return df

def changeType_date(df):
    df['inspection_date'] = pd.to_datetime(df['inspection_date'])
    return df

def fix_dates(df):
    """Fixes date format"""
    listFecha = ["inspection_date"]
    date_format = "mm/dd/aaaa"
    type_format = '%m/%d/%Y'
    
    listFecha2 = ["approved_date"]
    date_format = "mm/dd/aaaa"
    type_format = '%m/%d/%Y'

    changeType_date(df,listFecha, type_format)
    changeType_date(df,listFecha2, type_format)
    
    return df

def imputations(df):
    """Imputations of missing data"""
    df.house_number.mask(df.house_number.isna(), '0', inplace=True)
    df.street_name.mask(df.street_name.isna(), 'No especificado', inplace=True)
    df.zip_code.mask(df.zip_code.isna(), '0', inplace=True)
    df.x_coord.mask(df.x_coord.isna(), '0', inplace=True)
    df.y_coord.mask(df.y_coord.isna(), '0', inplace=True)
    df.latitude.mask(df.latitude.isna(), '0', inplace=True)
    df.longitude.mask(df.longitude.isna(), '0', inplace=True)
    df.borough.mask(df.borough.isna(), 'No especificado', inplace=True)
    df.result.mask(df.result.isna(), 'desconocido', inplace=True)
    df.location.mask(df.location.isna(), '(0.0, 0.0)', inplace=True)

    return df

def cleanning(df):
    df = clean_column(df)
    df = changeType_date(df)
    df = lowercase(df)
    df = imputations(df)
    return df