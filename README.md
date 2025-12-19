<header>
<img src="./images/5°-CIA-237x300.jpg" width=150 align="left"/>
<img src="./images/cuerpo-de-bomberos-maipu-300x289.png" width=150 align="right"/>
</header>
</br></br></br></br></br>

</br>
</br>

# FireFighter Department of Analytics

## Portafolio personal
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Alan-Grez/firefighter/master?urlpath=lab)

### Setup

Las instrucciones de uso se encuentran en [setup.md](setup.md).

Para usuarios de Windows que quieran aprovechar un entorno de desarrollo más cómodo, se recomienda revisar [wsl_ds_toolkit.md](wsl_ds_toolkit.md), que describe una configuración con WSL.

## Resumen del proyecto

Este repositorio reúne un proyecto de **predicción de servicios de emergencia** en el tiempo, con el objetivo de estimar:

- **Ubicación** del evento.
- **Fecha y hora** de ocurrencia.

### Datos considerados

- **Histórico**: servicios desde 2019 en adelante.
- **Resolución temporal**: hasta el minuto.
- **Intervalos**: registros con tiempos irregulares.
- **Identificación de servicios**: claves del tipo `10-X-Y`, donde:
  - `X` corresponde al tipo de servicio.
  - `Y` corresponde al subtipo.
- **Atributos por evento**:
  - Dirección, esquina y numeración.
  - Compañías que pueden participar: 1RA, 2DA, 3RA, 4TA, 5TA, 6TA, 7MA, 8VA, 9NA.

### Catálogo de llamados 10-X

- **10-0**: Llamado estructural.
- **10-1**: Llamado de vehículo.
- **10-2**: Llamado de pastizales y/o basura.
- **10-3**: Llamado de rescate de personas atrapadas.
- **10-4**: Llamado de rescate vehicular.
- **10-5**: Llamado de materiales peligrosos.
- **10-6**: Llamado de emanación de gases.
- **10-7**: Llamado eléctrico.
- **10-8**: Llamado no clasificado.
- **10-9**: Llamado a otros servicios.
- **10-10**: Llamado a escombros.
- **10-11**: Llamado a servicio aéreo.
- **10-12**: Apoyo a otro cuerpo.
- **10-13**: Llamado a atentado terrorista.
- **10-14**: Llamado a accidente aéreo.
- **10-15**: Simulacro.
- **10-16**: Llamado en túnel.

### Detalle de subclasificaciones y despachos

#### Incendios estructurales

- **1ª alarma**: 2 Bombas (b/bx), 1 Carro Aljibe (Z), 1 Unidad de Rescate (R).
- **2ª alarma**: 2 Bombas (b/bx), 1 Porta Escala (Q), 1 Escala Mecánica (M), 1 Carro Aljibe (Z), 1 Unidad de Rescate (R).
- **3ª alarma**: 4 Bombas (b/bx), 1 Unidad de Rescate (R).

#### Incendios de pastizales

- **1ª alarma**: 2 Bombas (b/bx), 2 Carros Aljibe (Z), 1 Unidad de Rescate (R).
- **2ª alarma**: 4 Bombas (b/bx), 1 Unidad de Rescate (R).

#### Llamados estructurales 10-0

- **10-0-1**: Inmueble hasta 4 pisos; se despachan 2 Bombas (b/BX) y 1 Porta Escala (Q).
- **10-0-2**: Inmueble de 5 pisos o más, o cualquier foco; se despachan 3 Bombas (b/BX), 1 Porta Escala (Q) y 1 Escala Mecánica (M).
- **10-0-3**: Conflicto en villas San Luis, Raul Massone, población La Farfana, Los Presidentes, Villa Joaquín Olivares, Santa Adela, El Trebal, el Maitén y Oeste Plat, Villa Matucana, Villa Bosqueado; se despachan 3 Bombas (b/BX), 1 Porta Escala (Q) para sector Buzeta y se agrega 1 Aljibe (Z).
- **10-0-4**: Para supermercados, centros de salud, comerciales y educacionales; se despacha 3 Bombas (b/BX), 1 Porta Escala (Q) y 1 unidad de rescate. Para inmueble de más de 4 pisos se agrega 1 Mecánica (M).
- **10-0-5**: Para industrias; se despacha 3 Bombas (b/BX), 1 Porta Escala (Q), 1 Unidad de Rescate (R) y 1 Unidad de Haz-Mat (H).

#### Llamado a vehículo 10-1

- **10-1-1**: 1 Bomba (B/BX/R1) para vehículos livianos hasta camiones ¾.
- **10-1-2**: Vehículos con transporte de gas, combustible o material peligroso (HazMat); se despacha 1 Bomba (b/BX), 1 Unidad de Haz-Mat (H) y 1 Unidad de Rescate (R).
- **10-1-3**: Vehículos de transporte de pasajeros sobre 15 personas (buses, microbuses); se despacha 2 Bombas (b/BX), 1 unidad de Rescate (R).
- **10-1-4**: Fuego en vagones de metro y/o trenes; se despacha 2 Bombas (b/BX), 1 unidad de Rescate (R).

#### Llamado a pastizales y/o basura 10-2

- **10-2-1**: 1 Bomba (b/BX). Para sectores que involucren cuarteles 1ª, 3ª y 6ª Cía. se priorizan los BX.

#### Rescate de emergencia 10-3

- **10-3-1**: Atropellos, caídas de altura, caídas sobre techo, árboles y/o estructuras de hasta 1 piso; personas en lecho de río o canal y/o caídas en desnivel; persona caída desde moto. Se despacha 1 Unidad de Rescate (R).
- **10-3-2**: Personas encerradas en ascensor, en inmueble de hasta 1 piso o al interior de vehículos. Se despacha 1 Bomba (B/BX) del sector.
- **10-3-3**: Personas encerradas en inmueble de hasta cuatro pisos; 1 Carro Bomba B/BX del sector.
- **10-3-4**: Personas encerradas en inmueble por sobre el 5 piso o sobre 10 metros; 1 Unidad de Rescate (R), 1 Mecánica (M).
- **10-3-5**: Personas atrapadas producto de derrumbes; 1 Bomba (b/BX), 1 Unidad de Rescate de 3ª Cía. (R-3) y 1 Unidad de Salvamento. Puede apoyar 1 Unidad de Rescate Urbano.
- **10-3-6**: Personas en caudal de río o canal, caídas en fosa o atrapadas en altura; 1 Unidad de Rescate (R), 1 unidad de especialidad (H-4 o R-3) para cuarteles 1ª, 2ª, 3ª y 7ª Cía. Cuarteles 4ª, 5ª, 6ª y 8ª Cía.: H-4.
- **10-3-7**: Personas atrapadas en vías de metro o tren (suicidio); 2 Unidades de Rescate (R).

#### Rescate vehicular 10-4

- **10-4-1**: Choque, colisión o volcamiento con máximo 2 personas atrapadas o 5 lesionados; 1 Bomba (b/BX) y 1 Unidad de Rescate (R).
- **10-4-2**: Choque, colisión o volcamiento con más de 3 personas atrapadas o 6 lesionados; 1 Bomba (b/BX) y 2 Unidades de Rescate (R).
- **10-4-3**: Choque, colisión o volcamiento de vehículos con materiales peligrosos; 1 Bomba (b/BX), 1 Unidad de Rescate (R) y 1 Unidad de Haz-Mat (H).
- **10-4-4**: Choque, colisión o volcamiento de vehículos de locomoción colectiva o camiones (buses urbanos y/o interurbanos, transporte escolar o camión de alto tonelaje); 1 Bomba (b/BX), 2 Unidades de Rescate (R).
- **10-4-5**: Choque, colisión o descarrilamiento de vagones de metro o trenes; 2 Bombas (b/BX), 3 Unidades de Rescate (R).

#### Llamados a materiales peligrosos 10-5

- **10-5-1**: 1 Bomba (B/BX), 1 Unidad de Rescate (R) y 1 Unidad de Haz-Mat (H).

#### Llamado emanación de gases 10-6

- **10-6-1**: Emanación de gases en domicilio o vía pública; 1 Bomba (b/BX) y 1 Unidad de Haz-Mat (H).
- **10-6-2**: Emanación de gases en centros de salud, comerciales, educacionales y supermercados; 1 Bomba (b/BX), 1 Unidad de Haz-Mat (H) y 1 Unidad de Rescate (R).

#### Llamado accidente eléctrico 10-7

- **10-7-1**: 1 Bomba (b/BX). Para sectores que involucren cuarteles 1ª, 3ª y 6ª Cía. se priorizan los BX.

#### Llamados sin clasificación 10-8

- **10-8-1**: 1 Bomba (b/BX).

#### Otros servicios 10-9

- **10-9-1**: Se despacha el material específico de la necesidad, previamente autorizado por el comandante de guardia.

#### Llamado a escombros 10-10

- **10-10-1**: 1 Bomba (b/BX), 1 Porta Escala (Q).

#### Llamado a servicio aéreo 10-11

- **10-11-1**: 1 Bomba (b/BX), 1 Unidad de Rescate (R).

#### Apoyo a otros cuerpos de bomberos 10-12

- **10-12-1**: Se despachará material de acuerdo a lo solicitado.

#### Llamado actos terroristas 10-13

- **10-13-1**: 1 Bomba (b/BX), 1 Unidad de Rescate (R), 1 Unidad de Haz-Mat (H).

#### Llamado a accidente aéreo 10-14

- **10-14-1**: 1 Bomba (b/BX), 2 Unidades de Rescate (R).

#### Simulacro 10-15

- **10-15-1**: Se despachará material relativo a la naturaleza de cada acto.

### Objetivo

Usar estos datos para modelar y anticipar emergencias reales en las que asisten bomberos.
