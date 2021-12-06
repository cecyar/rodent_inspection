![](https://lh3.googleusercontent.com/proxy/nJHMyK845YMo3gHd1CzaT-As-oV-WIxmBkvyF0d9x-OFcfwWgJHXWHODydp8VhCMAbqu1_DU6Gl5KL4g2juIW3wSGKmVdKs_rVfCDFaxK97h4Ot-dps)

## Estadística Computacional (Otoño 2021)
## QUARANTEAM, Proyecto Final: Rodent Inspection
	
### Integrantes del equipo

| Nombre                           |  CU    | Mail               | Usuario Gh |
|----------------------------------|--------|--------------------|------------|
| Luz Aurora Hernández Martínez    | 178831 | lhern123@itam.mx   | LuzVerde23 |
| Ita-Andehui Santiago Castillejos | 174134 | isantia2@itam.mx   | sancas96   |
| Cecilia Avilés Robles            | 197817 | cavilesr@itam.mx   | cecyar     |
| Leonardo Ceja Pérez              | 197818 | lcejaper@itam.mx   | lecepe00   |

## Pregunta analítica a contestar
Pasará una propiedad una inspección de ratas o no

# Comprensión del negocio
Consulte el documento [00_comprension_negocio.md] (https://github.com/cecyar/rodent_inspection/blob/main/00_comprension_negocio.md)

# Base de datos
La base de datos que se analizará en este trabajo será la de [Rodent inspection](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj) obtenida de [NYC Open Data](https://opendata.cityofnewyork.us/). 

# Reproducibilidad y requerimientos. ⚙️

**Importante** Este proyecto debe ser ejecutado desde el ambiente de trabajo seleccionado, ejecutando `pyenv activate <<tu_ambiente>>`.

# Infraestructura

Para este proyecto utilizamos la versioń **Python 3.8**
1. Para la reproducibilidad del análisis exploratorio de datos: en la carpeta data, colocar el archivo `Rodent.csv` que está disponible en este [**Drive**](https://drive.google.com/file/d/1JCXlYAfIUP7xOGPAxS-MUKE1sNXJMWKl/view?usp=sharing)
2. guárdenlo en la carpeta data del repo
3.  en la raíz del repo, ejecuten estos dos comandos:  
    3.1.  awk -f src/utils/clean_data.awk < data/rodent.csv
    3.2.  sed -r '/(^|,)\s*(,|$)/d' data/rodent_reduced.csv > src/utils/Rodent_Inspection.csv
4.  hagan make build y make up, y el SQL ya debe tener los 200K registros limpios (al final son poquitos menos, como 196k porque se eliminaron todos los que tenían faltantes)

# EDA
Puede consultar el [análisis exploratorio de datos](https://github.com/cecyar/rodent_inspection/tree/main/notebooks)

# Entrenamiento
Puede consultar el [Entrenamiento de modelos](https://github.com/cecyar/rodent_inspection/blob/main/notebooks/Model_rodent.ipynb)

