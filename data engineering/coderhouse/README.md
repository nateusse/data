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
    - DB que almacena mucha info para ser analizada
    - Relacional, rapida consulta SQL. Estructura planificada
    - Datos estructurados y muchos tipos de diferentes fuentes.

- Data Mart
 - Set de tablas para un area de la compania. Datos resumidos para cada area


- Data Lake
    


4. Normalization, facts, dimension and types of esquems, 