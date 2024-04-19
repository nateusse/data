# DATA SCIENCE

# Bases de datos relacionales

- HISTORIA: 
    Creadas por IBM, 80's. Relaciones entrer tabals son esquemas
    Recolecta datos en una tabla virtual llamada vista
    Idealmente basese de datos trasnsaccional, OLTP, rapida, tiempo real.
    Crear secuencia de comandos que suba datos al warehouse otimizado para procesamiento analitico
    Nasa, datos masivos que exceden hardware que los almacena. Muchas empresas no tienen datos masivos, no porque sean muchos o so sepa como almacenaros, son masivos si (Volumen, veraces, variedad, velocidad)

- ETL:  Extraccion, trasnformacion y carga al warehouse para analisis 

- Hadoop: 
    Remplaza warehouse, subir ETL a cluster Hadoop, ahorrarse nube. Tiene NoSQL, llamada HBase
    Limitaciones de SQL que resuelve Hadoop: No flexibles, necesitan esquemas (conocer formato, organizarlos en tablos y organizar relaciones)
    NoSQL : No esquemas, util para clusters, codigo abierto, no noramlizar, apta para clusteres.
    Los registros se guardan en agrergados (con toda la info), puedo sincronizarlos con clusteres.


Volumen: Petabytes y Exabytes. Normales son kilobytes, megabytes, gigabytes, terabytes.
Veraces: Me ayuda a resolver mi problema
Variedad: Stocks market is not
Velocidad:


# Tipos de datos

- Estructurados: Inflexibles, modelo de datos para definir campos individuales (exto, numero, fechas..) Bases relacionales
- Semiestructurados: Mismo modelo, diferentes esquemas. Estructura depende de la fuente, la empresa por ejemplo. Formatos son XML, JSON para web
- No structurados: Fotos, audios, ... Vision de 360 del cliente (conocerlos, enviarle promociones, formular preguntas adicionales)


# Estadistica
- Estadistica narra una historia, deescriptiva, usar media y mediana. si hay una diferencia muy grande los datos estan sesgados
- Probabilidad: Medicion resultados posibles
- Correlacion: Grado de relacion entrer 2 variables. Medible entre 1 y 0
    No implica causalidad
- Analitica predictiva: Predecir futuro a aprtir de bases hisroticos. 
