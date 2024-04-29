# Youtube Machine learning con Python


## LIbrerias
### Numpy (numerical python)
- pip install numpy, import nympy as np
- Matrices N-dimensional
    - Unidimensional, 1D [() ]
    - Bidimensional 2D [(),() ]
    - 3D 3 ejes, axis 2
- np.array vs array
    - np.array[] ocupa menos espacio, es mas rapida
- methods:
    - array = np.array([1,2,3,4 ],[5,6,7,8 ] dtype = np.int64)  #[[1,2,3,4 ],[5,6,7,8 ]]
    - np.ones((2,4))  #[[1. 1. 1. 1.], [1. 1. 1. 1.]]
    - np.zeros((2,4))  #[[0. 0. 0. 0.], [0. 0. 0. 0.]]
    - np.random.random((2,2))  #[[0.43234  0.23423],[0.32423  0.234234]]
    - np.empty((3,2)) # [[0. 0.],[0. 0.],[0. 0.]]
    - np.full((2,2),8)  # [[8 8],[8 8]]
    - np.arange((0,30,5))  #[0 5 10 15 20 25 ]
    - np.linspace(0,2,5) # [0. 0.5 1. 1.5 2]  aleatorios de 0 a 2, 5 en total
    - np.eye(4,4)   #matrices identidad
    - np.identity(4)
    - variable.ndim  #dimensiones
    - variable.dtype
    - variable.reshape(3,2) #pasa de [[8, 9,10],[11, 12,13]] a [[8, 9],[10, 11],[12, 13]]
    - varible[0 , 2]  # de la variable 0 el segundo elemento empezando desde 2
    - variable[0: ,2] #desde la fila 0 en adelante, todos, tomar valores 2 tecnicamente 3 por emepzar dedse - Ej [3 5] en array bidimensional
    - variable.min()  .max() .sum()  
    - np.sqrt(variable), np.std(variable)


### Pandas (panel data) 
- pip isntall pandas , import pandas as pd
- Acciones:
    - Cargar, preparar, analizar, modelar y manipular DF
- Series
    - Matrices unidimensionales con indices
- Data Frame
    - Estructuras de datos bidimensionales, con indices en columas y filas
    - Tiene datos, indeces y columnas


### Bias y varianza
- Errores de prediccion
    - BIAS o sesgo.  Poco flexibles y de menor rendimiento. Alta bias requiere muchas suposiciones(regresion lineal,analisis discrecionales lineal y regresion logistica), baja Bias son arboles de decision, k-vecinos, maquinas de vectores de soporte
    - Error de varianza - A diferentes datos de entrenamiento, la estimacion cambia. Hay varianza alta (cambia mucho segun datos de entrada como regresion lineal, analisis discriminate y logistico) y baja (arboles de desicion, k-vecinos, maquinas vectores)
    - Error irreducible o ruido (por problem mal enmarcado, variables desconocidas, caracteristicas incompletas)

