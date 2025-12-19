<header>
<img src="./images/5°-CIA-237x300.jpg" width=150 align="left"/>
<img src="./images/cuerpo-de-bomberos-maipu-300x289.png" width=150 align="right"/>
</header>
</br></br></br></br></br>

</br>
</br>


# FireFighter Departament of Analítics.

## Portafolio Personal
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Alan-Grez/firefighter/master?urlpath=lab)

### Setup

Las instrucciones de uso se encuentran en [este](setup.md) siguiente archivo. 

Para aquellos usuarios de Windows que quieran sacar partido, se recomienda mirar también [este](wsl_ds_toolkit.md) archivo, mostrando un entorno de trabajo con WSL.

## Reseña del proyecto

Este repositorio alojará un proyecto de predicción de servicios de emergencia a lo largo del tiempo, estimando tanto la ubicación como la fecha-hora de ocurrencia. La propuesta considera el histórico de servicios desde 2019 en adelante, con tiempos en intervalos irregulares y resolución máxima al minuto. Los servicios se identifican por claves del tipo 10-X-Y, donde X corresponde al tipo de servicio e Y al subtipo. Para cada evento se cuenta con dirección, esquina y numeración, además de las compañías que pueden participar (1RA, 2DA, 3RA, 4TA, 5TA, 6TA, 7MA, 8VA, 9NA). La intención es usar estos datos para modelar y anticipar emergencias reales en las que asisten bomberos.
