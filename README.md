ih_datamadpt0522_project_m1

**BICIPARK🚲 🏞️**

**¿QUÉ ES ESTO DE BICIPARK?**

Este proyecto consiste en un programa donde el usuario introduciendo un parque de la Comunidad de Madrid, recibe la estación de bicis de la Comunidad de Madrid   

**🏅GOALS**

El resultado que le damos al usuario despues de introducir el parque de interes, es la distacia y la estación de bicis más cerana.

Tambien, el usuario tiene la opción de recibir mediante un archivo csv, todo el directorio de parques de la Comunidad de Madrid con su correspondiente escación de bicis más cercana.

**📉The dataset**

El conjunto de datos utilizado para este proyecto lo dividimos en dos partes.

Conjunto de datos de Bici MAP, lo podemos encontrar aquí: mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD
Conjunto de datos de los parques de la Comunidad de Madrid: https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json

**💥Technical procedure**
  
Conjunto de datos Bici_MAD: Primero de todo tuve que conectarme a la base de datos de BiciMap a traves de SQL, teniendo en cuenta las creedenciales aportadas y lo transformamos a Dataframe a traves de una consulta.

Conjunto de datos de Parques y Jardines de la Comunidad de Madrid. Transformamos el Json a un Dataframe.

Una vez hemos convertido los conjuntos de datos al mismo formato, empezamos a trabajar con ellos, en busca del resultado comentado anteriormente.


**🏃 Demo-pipeline**

Mi codigo necsita como minimo 1 argumento de entrada, en caso de que el usuario quiera el directorio completo. En el caso de que quiera un parque en concreto, necesitaremos 2 input por parte del usuario.


**💻 Technology stack**

SQL, 
Python,
Sqlalchemy 
Pandas 
Requests
Math
Jupyter Notebook
Visual Studio Code

**🔧 Configuration**

Para poder realizar este proyecto, necesitamos Jupyter Noteobook, Visual Studio Code, crearnos un entorno donde instalemos todas las librerias.

**📁 Folder structure**

└── project
    ├── README.md
    ├── .gitignore
    ├── .Project_M1_API
    ├── .Project_M1_SQL
    ├── .Uion_Project_m1
    ├── .BICIMAP
    ├── .results_1
    ├── .results_2
   
**Next Step 💪
**
- Que el usuario ademas de recibir la información deseada por CSV, reciba un mapa con la ruta entre el parque y la estación de bicis 🗺
- Que el usuario no tenga que introducir el nombre completo del parque

**💌 Contact info**

Mail: fco.villalobos.perez@gmail.com Obtener ayuda, involucrarse, contratarme por favor.
- 


