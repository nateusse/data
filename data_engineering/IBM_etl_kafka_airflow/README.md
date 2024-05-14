# COURSERA - IBM ETL and Data Pipelines with Shell, Airflow and Kafka

1. Processing techniques
- Objetivos: QUe es ETL y ELT, batch vs stream laoding, data laoding tecniques, examples of raw data

- ETL: Curar data para integrar a una paltaforma (data warehouse o analytics environment)
- ELT: Load data in raw format. Automated data pipeline methodology
    - Extraction: Read u obtains data from 1 o mas sources
        - Web scraping: Python para parse HTML
        - APIs
        - Edge computing para redicir raw data repetida de IoT, extraer lo interesante
        - Biomedical devices
        - OCR (optical character recognition): Scanear
        - Streaming (social media feeds, IoT, weather) or static (archivos) como en batch process
        - Mail, cookies, 
        ADC (analog to digital, ) CCD (Charge-couple devices )
        - Raw data (papers, web apges, audio, video, surveys, transactional data, social media, weather, IoT, medical records, human genomes)

    - Load: Cargar data en envoronment
        - Database, data warehouse, data mart
    - Transformation or wrangling: POnerla en un formato para : Ser procesada y targed systems
        - Cleaning (fixing errors or missing value, duplicatess)
        - Noramlizing: COnvertir data a unidades comunes
        - Filtering (solo lo necesario, sorting, agregation, binning)
        - Joining different data sources
        - Feature enginering (dashboards, machine learning)
        - Foarmating o structuring (data complatible con el destino, JSON, XML, CSV)
        - data typing (fload, integrer)

- USOS ETL: 
    - Concetar diferentes sources distribuidos
    - Same source (mover data es un camello)
    - No information lost
    - Separa data pipeline del procesamiento (mas flexible)
- ELT vs ETL
    - Transformacion pipeline
    - Rigidez, slef serve analitical
    - Escalabilidad, ETL es relacional, no maneja unestructured
    - On premise vs Cloud
    - Time, trasnfomar toma tiempo

2. ETL and data pipelines: Tools and techiques

- Objetivos: Shell, data pipeline definition, mitigar data flow bottlenecks, batch vs streaming data pipelines
- OLAP vs OLTP: 
- ETL runs in batches, trigger by events not periodically
- INtegracion de ssitemas ocurre en stagin area
- DAGs (directed acyclic graph) Lo que usa Airflows para representar el workflow, divide y reinaras, usando operators (como templates)
- TOOLS: Talend, AWS GLue, alteryx, Airflow, pandas

- Airflow: Open source Airbnb, "configuraiton" as code, 

- SHELL: Scripting language, Unix-like
- WORKFLOW ETL with Shell: 

- Extraer data

    - CUT : Extract selected characters or fields from a line of text.
        - echo imprime en terminal
        - echo "baracunatana" | cut -c1-4 (extraer primero 4 letas de la palabra en "" de 0 a 3)
        - echo "database" | cut -c5-8 (letras del 5 al 8)
        - echo "database" | cut -c1,5 (1 y 5 SOLAMENTE)
        - cut -d":" -f1,3,6 /etc/passwd (-delimeter and -fild number) vs cut -d":" -f3-6 /etc/passwd
    - TR: Translate, squeeze, and/or delete characters.
        - echo "Shell Scripting" | tr "[a-z]" "[A-Z]" echo "Shell Scripting" | tr "[:lower:]" "[:upper:]" (minusculas a MAYO)
        - ps | tr -s " "
    - -d
        - echo "My login pin is 5634" | tr -d "[:digit:]" (delete digits)

3. Building data pipelines using AirFLow
- Objetivos: Airflow, python scripts for Airflow DAG objects, workflow as a code, identificar DAGS y set up dependencies

4. Building streaming pipelines using Kafka
- Objetivos: Kafka as event streaming paltaform, end-to-end streaming plataform example, describir kafka API.


5. Project