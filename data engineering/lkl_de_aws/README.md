# AWS & DATA ENGINEERING

## Data lake
- Advantages:
    - Squema on read
    - Single source of true. Ej: S3  for data lake consumed by EC2 and Lambada, redshift for  analysis
- Architecture
    - Decouple (ingestion, consumption, and processing)
    - Identify hot, warn and cold data (used a lot or not)
    - Right tool for right job
    - Event journal design pattern, (Ej: not delete data once store)
    - Cost

## Pipeline
### Data source
- **DynamoDB**
    - Uses
        - Gamming
        - Mobile
        - Digital ad services
        - Live voting
        - AUdience interaction for live envents
        - Metadata storage for S3
        - Sensor network
        - Access control for web
        - E-coomerce shopping cart
        - Web session management
    - Antipatterns
        - Complex joins or transactions
        - Schemas
        - Large size objects   
    - Key features
        - Multi-region (data is replicated accross 3 different zones, no need to patch or upgrade)
        - NoSql (Schemaless)
        - Autoescaling
    - Procedimiento
        - Crear tabla, sin encesidad de definir atrubutos en rows
        - 400 kylabites (KB) max per row, infunidad de rows, S3 5 terabyeste
        - RCU (read capacity unit) and WCU (write capacity unit) pueden ser calculados en capacity calculator

### Ingestion
- Insert multiples type of data, batch, real time, data bases..
- COnsiderations
    - Format. H ow data is comming
    - Type of data
    - Data frecuency 
    - Optimal size (16 and 256 MB), compact small KB into bigger ize
    - File format. Oarquet and ORC 
    - Partitioning
    - Ingestion parttern (right tool)
- Hibrid 
   - Usualmente clientes quieren hibrid para no rehacer toda la arquitectura (on premise mas cloud).
   - Manteer the set up, cloud and on-premise. Talk to each other
   - Opciones:
        - Data connect (primavete connection in my on-premise)
        - storage gateaway (Yo instalo, para store y comunication with cloud)
- Migrar: 
    - Snowmobile shipped to yoru location put in this device and ship to amazona gain. 
    - Data migration service (DMS)
    - Taad sink
- Real time ingestion or batch
    - Real time data: Kinesis (Kinesis strerams, Firehose, kafka)
        - Kinesis:
            - Connect, process, analyze types of data streams (event logs, social media feeds, clickstram data, sensors,..)
            - Control by IAM to access
            - AWS KMS (data at rest protection at S3 and redshift)
            - roteccion in transit: TLS (transport layer security protocol for data in trasnti)
            - Services:
                - Amazon kinesis video streams (audio, videos)
                - Amazon kinesis data streams (Base64-eoncded data,clicks, logs, feeds, trasnactions, in game , IoT sentos)
                - Amazon kinesis data firehose
                - Amazon kinesis data analytics
    -  Batch: AWS Glue jobs, or third-sparties such Sparks