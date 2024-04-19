# DATA ENGENEERING CODERHOUSE

1. Welcome
- Installation Docker, Dbeaver
- Practice python and SQL

2. Intro Data Engineering 

- Historia:
    - Censo Estados Unidos tomaria anos, Herman Hollerith, 80's crea maquinas tabuladora.
    - Big Data: Volumen (fuck excel), Velocity (senrores, fraude), Variedad
    Facebook, AirBnB - Infrestructura de datos, warehousing, data mining, modelado de datos, seguridad de los datos.

Tareas: Mantenimiento datos nube, generacion modelo de datos para analistas y cientificos de datos, seguridad informatica.

- Roles: 
    - Data analist: Genera graficos y metricas sobre el negocio
    - Data science: Modelos predictivos 
    - Data Engeneering: Ingeniero  q' resuleve problemas con grandes cantidades de datos. hace dats accesible.
    Automatiza datos, le da sentido logico
    
- Sistemas:
    - OLAP: Online anaytlical processing
        - Lectura gran escala para consultas analiticas, todos los registros, el tiempo , no normalizados
        - Ej: E- commerce
        - Cientificos de datos, analistas
        - SELECT, INSERTS masivos 1 ves al dia ETL
    - OLTP: Online transaction processing. 
        - Mas comunes y antiguos. Escritura trsnacicones y lectura datos esecificos. 
        - Ej: Sistemas bancarios
        -  INSERTS, UPDATES a veces DELETE

- Arquitectura bases de datos
    - Tier 1: Usiarios usan db, pueden modificarla
    - Tier 2: Usiario conecta db con APIS, ODBC y JDBC, cliente no misma maquina db
    - Tier 3: Capa logica y capa de datos para concetar con ussuario. Comun en web
    - Tier 4: Multiplayer. Web server, web container y application server

- Acessos:
    - Centralizados: Sola ubicacion. Conexion acceso internet LAN, WLAN..
    - Desentraliados: Red de compmutadoras distrubiodas

3. DataWarehouse and ETL

- DataWarehouse:
    - Solamente datos estructurados en SQl
    - DB que almacena mucha info para ser analizada
    - Relacional, rapida consulta SQL. Estructura planificada
    - Datos estructurados y muchos tipos de diferentes fuentes.

- Data Mart
 - Set de tablas para un area de la compania. Datos resumidos para cada area


- Data Lake
    - Sistemas distrubidos que almacenan datos estructurados, semisestructurados (json) y no estructurados (texto, video)
    
- ETL
    - Extraer: Tomar info de todas las bases de datos
    - Cargar: Transferirlos a un sistema unico
        - Apache Flink, Apache Bean, Redis, Kafka
    - Trasformar: Normalizarlos, limpiearlos y prepararlos para analisis. Modificando datos nulos, campos vacios, datos incoherentes y duplicados, tipo incorrecto.
        - Se transofrman con pipelines (procesos ornedaos y rutinas) , son idepmpotencia (generar el mismo resultado) cada cierto tiempo
        - Usa Engines: Modificar, anadir y limpiar: Apache  Spark, Apache Hadoop

    - Oquestacion de procesos:
        Apache Airflow, Azure data factory

 - Tipos de datos a ser trasnformados:
    - Batch: Asincronas. Ej: bases de datos que llegan 1 vez al dia por ejemplo
    - Tiempo real: Casi sincrona. Ej: Sensores


 


4. Normalization, facts, dimension and types of esquems, 