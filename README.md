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
¿Pasará una propiedad una inspección de ratas o no?  Entiéndase, ¿se encontrarán ratas en dicha propiedad?

El modelo consiste en una clasificación binaria con las siguientes etiquetas:

- `Etiqueta 0:`  La propiedad **SÍ** pasará la inspección de ratas (no se encontrarán ratas en la propiedad).
- `Etiqueta 1:`  La propiedad **NO** pasará la inspección de ratas (sí se encontrarán ratas en la propiedad.)

# Comprensión del negocio
Consulte el documento [00_comprension_negocio.md](https://github.com/cecyar/rodent_inspection/blob/main/00_comprension_negocio.md)

# Base de datos
La base de datos que se analizará en este trabajo será la de [Rodent inspection](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj) obtenida de [NYC Open Data](https://opendata.cityofnewyork.us/).

# Infraestructura y Ejecución ⚙

Para ejecutar este producto de datos se necesita lo siguiente:
- Sistema operativo Linux/Mac con Docker Desktop instalado.
- Clonar el repositorio en el equipo.

**Para levantar la imagen de docker y la base de datos:**
1. Descargar el archivo `Rodent.csv` que está disponible en este [**Drive**](https://drive.google.com/file/d/1JCXlYAfIUP7xOGPAxS-MUKE1sNXJMWKl/view?usp=sharing), y colocarlo en la carpeta `data` del repositorio.
2. Limpieza de datos: 
   1. En la raíz del repositorio, ejecutar estos dos comandos:
      1. awk -f src/utils/clean_data.awk < data/rodent.csv
      2. sed -r '/(^|,)\s*(,|$)/d' data/rodent_reduced.csv > src/utils/Rodent_Inspection.csv
3. Construir la imagen de docker:  
   1. En la raíz del repositorio, ejecutar estos 2 comandos:
      1. make build
      2. make up
4. Para visualizar la tabla generada de la base de datos:  
   1. Abrir el explorador de internet e ir a la siguiente dirección:
      1. localhost:5000/home.
         1. **Nota:**  Debido al tamaño de la tabla (aprox. 196K registros), puede generar errores después de cargar una gran cantidad de filas.  
5. Para visualizar la base de datos utilizando el servicio de `pgAdmin`:  
   1. Abrir el explorador de internet e ir a la siguiente dirección:
      1. localhost:8000
   2. Después de visualizar la pantalla de bienvenida de `pgAdmin`, ingresar los siguientes datos:
         1. username:  admin@admin.com
         2. password:  admin
   3. Después de entrar al servicio de `pgAdmin`, dar click derecho sobre `Servers` en el menú de la izquierda, seleccionar `Create` y posteriormente `Server`.
   4. En la ventana que se despliega, capturar la siguiente información:
      1. Pestaña `General`: Darle nombre al servidor, por ejemplo: `Rodent`.
      2. Pestaña `Connection`:  
         1. Host name:  db
         2. Username:  root
         3. Password:  root
   5. Debe ser posible visualizar la tabla `api_model`, que contiene todos los registros de nuestro dataset.

**Entrenamiento del modelo:**
1. Ejecutar el notebook [Model_rodent.ipynb](https://github.com/cecyar/rodent_inspection/blob/main/notebooks/Model_rodent.ipynb) en la carpeta `notebooks` del repositorio.

**Uso del modelo de predicción:**
1. En el explorador de internet, ir a la siguiente dirección:
   1. localhost:5000/prediction
2. Ingresar los siguientes datos para generar la predicción:
   1. `Job ID`:  Identificador de la inspección, valor numérico de 7 dígitos.
   2. `Boro Code`:  Identificador numérico del distrito de Nueva York a inspeccionarse, 5 valores numéricos posibles:
      1. Manhattan (1)
      2. Bronx (2)
      3. Brooklyn (3)
      4. Queens (4)
      5. Staten Island (5)
   3. `Zip Code`:  Código postal donde se realizará la inspección, valor numérico de 5 dígitos.
   4. `Latitude`:  Latitud donde se realizará la inspección, valor numérico (aprox 48.XXXX para la ciudad de Nueva York).  
   5. `Longitude`:  Longitud donde se realizará la inspección, valor numérico (aprox -73.XXXX para la ciudad de Nueva York).
   6. `Inspection type`:  Tipo de inspección a realizarse, seleccionar alguna de las siguientes opciones:
      1. Bait
      2. Clean up
      3. Compliance
      4. Initial
      5. Stoppage
   7. Posteriormente, dar click en el botón `Submit`, y el modelo arrojará la etiqueta predicha.

# EDA
Puede consultar el [análisis exploratorio de datos](https://github.com/cecyar/rodent_inspection/tree/main/notebooks)

**Nota:**  Este análisis exploratorio se realizó con el dataset original con los registros al 16 de Noviembre de 2021.  El dataset original cuenta con más de 2 millones de registros.  

Para facilitar la ejecución del producto de datos, el producto de datos utiliza un dataset reducido de aproximadamente 200,000 registros, disponible en el [**Drive**](https://drive.google.com/file/d/1JCXlYAfIUP7xOGPAxS-MUKE1sNXJMWKl/view?usp=sharing) mencionado anteriormente.

# Entrenamiento
Puede consultar el entrenamiento del modelo de predicción en el notebook: [Model_rodent.ipynb](https://github.com/cecyar/rodent_inspection/blob/main/notebooks/Model_rodent.ipynb).

