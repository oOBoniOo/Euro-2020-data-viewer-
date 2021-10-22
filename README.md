<img src="https://api.brandy.run/core/logo" width="80"/>

# Proyecto Mid-Bootcamp

## EURO-2020 Data

> Obtendremos diferentes datos de la base de datos de la euro 2020 de kraggle y la mejoraremos con mas datos scrapeados de la web.

## Comenzando 🚀

### Pre-requisitos 📋

   > Usaremos librerias os, dotenv, numpy, pandas, flask, streamlit,fpdf.

## DATA
   > https://www.kaggle.com/mcarujo/euro-cup-2020  datos de los partidos de la eurocopa

   > https://www.fifaindex.com/ datos de jugadores y clubs

   > https://www.goal.com/en-qa/lists/euro-2020-squads/ datos de convocatorias completas.

  >  /data_support, estan las herramientas usadas para obtener datos.


## API ⚙️

    _Disponemos de los siguientes endpoints /src/controllers:
        * /matchs (devuelve todos los partidos)
        * /matchs/search devuelve partidos de una selecion o fase{stage,team}
        * /matchs/list_sel devuelve lista de selecciones

        * /player (devuelve jugador aleatorio o por nombre{name})
        * /player/search {name, pos, club}
        * /squads/list (devuelve lista de seleciones)
        * /squads (todas las convocatorias)
        * /team (devuelve un equipo)

    usamos los archivos en /utils para conexion a bd y conversion de datos.



## Desarrollado con con 🛠️

* [Jupiter-notebook](https://jupyter.org/) - El framework web usado
* [Visual Code Studio](https://code.visualstudio.com/) - Editor
* 


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)
## Autores ✒️

* **Daniel Bonillo** - *Trabajo Inicial* - [villanuevand](https://github.com/oOBoniOo)
* **Alvaro** - *Ayuda y soporte* - [alvaro](#fulanito-de-tal)
* **Felipe** - *profe* - [alvaro](#fulanito-de-tal)

