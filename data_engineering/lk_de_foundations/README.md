# DATA ENGENEERING FOUNDATIONS


1. Intro
    - Solve problems such as gather info from different sources, optimized for analyses, remove corrupt files, repair and automitezed pipelines. Imagine a Data Science problem working with legacy code, scattered data, inifficient storage, slow process
    - Should use linux, cloud, Python, SQL, distrubuted systems
    - Builds robust and scalable data arquitecure, cleans data
    - Uses:
        - DB: SQL , NoSQL
        - Processing frameworks: Data cleaning, clustering (varias maquinas), batch and streram processing. Spark, Hive, Flink, Kafka
        - Automation, Scheduling tools: Airflow, Oozie, Luigi, Cron

2. Databases and dataframes
    - DBMS (data abse maangment system) helps CRUD
    - File system VS DB: DB Organizacion eficiente, CRUD, files menos funcioanlidades
    - DB structured: Relacion / Semi-structured: JSON / Unistructured: Videos, Images, text files
    - SQl VS NoSQL: SQL stores in tables
    - SQL Schema:
        - Star: A fact tables (hecho que paso), que referencia a dimension tables (mas info)  Ej: Redshift es bueno para almacenarlas
    
    - Distrubiting computing
        - Distrubir sub-tasks en diferentes computadores no expensive y merge resultado
        - Problemas: Muchas unidades requeridas, overhead comunicar nodos ( parallel slow down)

3. Tools
    - Framework: Hadoop. Distributed processing of large data sets across clusters of computers
    - Processing technique: 
        - MapReduce based in Java. Distribuir entre several computer en el cluster, dificil de escribir
        - Hive: Layer de Hdoop, para hacer queries, extraer data fron DB y files
        - Spark: Mapreduce costoso, Spark ahorra proceso  en la misma memoria. Cuenta con Resilient Distributed DataSet (RDD), como estructura de datos para mantener data across muchos nodos, son inmutables
        - AirFlow
        - Distributed File System (HDFS); Archivos reside en multiples computadoras, remplazado por GCS (google cloud storage) and S3 de Amazon

4. ETL Pipelines



