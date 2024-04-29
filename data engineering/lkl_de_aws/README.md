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

- **S3**